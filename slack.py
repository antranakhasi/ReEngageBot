from slack_bolt import App
from hubspot import search_deals, create_task_for_deal
from config import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET
import threading

app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)

def process_reengage(respond, property_name, property_value):
    try:
        deals = search_deals(property_name, property_value)
        if not deals:
            respond(f"No deals found with `{property_name} = {property_value}`.")
            return

        count = 0
        for deal in deals:
            try:
                create_task_for_deal(deal, note=f"Re-engage deal {deal['id']}")
                count += 1
            except Exception as e:
                owner = deal['properties'].get('hubspot_owner_id')
                print(f"⚠️ Failed for deal {deal['id']}, owner={owner}: {e}")

        respond(f"Created {count} re-engagement tasks for deals with `{property_name} = {property_value}`.")

    except Exception as e:
        respond(f"⚠️ Error while searching deals: {e}")

@app.command("/reengage")
def handle_reengage(ack, respond, command):
    ack()
    text = command.get("text", "").strip()
    args = text.split()

    if len(args) < 2:
        respond("Usage: `/reengage <property> <value>`")
        return

    property_name = args[0]
    property_value = " ".join(args[1:])
    respond(f"Searching deals where `{property_name}` = `{property_value}`...")

    # Run in a separate thread so Slack doesn't timeout
    threading.Thread(
        target=process_reengage,
        args=(respond, property_name, property_value),
        daemon=True
    ).start()

if __name__ == "__main__":
    app.start(port=3000)