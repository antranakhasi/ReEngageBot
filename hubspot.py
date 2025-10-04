import requests
import time
from config import HUBSPOT_API_KEY

BASE_URL = "https://api.hubapi.com"
HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_API_KEY}",
    "Content-Type": "application/json"
}

def search_deals(property_name, property_value, limit=100):
    """Search deals where property_name equals property_value"""
    url = f"{BASE_URL}/crm/v3/objects/deals/search"
    payload = {
        "filterGroups": [
            {"filters": [{"propertyName": property_name, "operator": "EQ", "value": property_value}]}
        ],
        "properties": ["dealname", "hubspot_owner_id", "priority"],
        "limit": limit
    }
    resp = requests.post(url, json=payload, headers=HEADERS)
    resp.raise_for_status()
    return resp.json().get("results", [])

def create_task_for_deal(deal, note=None):
    deal_id = int(deal["id"])
    props = deal["properties"]
    owner_id = props.get("hubspot_owner_id")
    dealname = props.get("dealname", str(deal_id))
    priority = props.get("priority", "MEDIUM").upper()
    if priority not in ["LOW", "MEDIUM", "HIGH"]:
        priority = "MEDIUM"

    if not owner_id:
        raise ValueError(f"Deal {deal_id} has no owner; cannot assign task.")

    import time
    due_timestamp = int((time.time() + 2*24*60*60) * 1000)

    # Step 1: create the task
    payload = {
        "properties": {
            "hs_task_subject": f"Re-engage {dealname}",
            "hubspot_owner_id": owner_id,
            "hs_task_body": note or f"Re-engage deal {deal_id}",
            "hs_task_status": "NOT_STARTED",
            "hs_task_type": "TODO",
            "hs_task_priority": priority,
            "hs_timestamp": due_timestamp
        }
    }

    url = f"https://api.hubapi.com/crm/v3/objects/tasks"
    resp = requests.post(url, json=payload, headers=HEADERS)
    resp.raise_for_status()
    task = resp.json()
    task_id = task["id"]

    # Step 2: associate task with deal
    assoc_url = f"https://api.hubapi.com/crm/v3/objects/tasks/{task_id}/associations/deal/{deal_id}/task_to_deal"
    assoc_resp = requests.put(assoc_url, headers=HEADERS)
    assoc_resp.raise_for_status()

    return task