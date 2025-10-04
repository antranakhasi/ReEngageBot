# ReEngageBot
## 1. What It Does
- Users run `/reengage <property_name> <property_value>` in Slack.
- The bot searches HubSpot deals where the specified property equals the given value.
- For each matching deal:
  - Creates a task in HubSpot.
  - Assigns the task to the deal owner.
  - Associates the task with the corresponding deal.
  - Handles multi-word property values.
- Responds back in Slack with:
  - Number of tasks created.
  - Any errors (e.g., if a deal has no owner).

### Why it’s useful
If you are a small company or business and your product evolves or new features are added, you don’t want to manually go back to HubSpot to re-engage customers you previously reached out to about a feature. This bot automates that process, ensuring your team can follow up efficiently and maintain consistent customer engagement—helping your team perform better without extra manual work.

---

## 2. Tech Stack
- Python 3.9+
- Slack Bolt (`slack_bolt`) — for Slack interactions
- Requests — for HubSpot API calls
- HubSpot CRM API v3
- Optional: ngrok for local HTTPS tunneling

---

## 3. Repository Structure

ReEngageBot/  <br>
├── app.py           # Starts the bot and ngrok tunnel  <br>
├── hubspot.py       # HubSpot API integration (search deals, create tasks)  <br>
├── slack.py         # Slack command handler (/reengage)  <br>
├── config.py        # Loads Slack & HubSpot credentials from environment  <br>
├── requirements.txt # Python dependencies  <br>
└── README.md        # This file  

---

## 4. Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/yourusername/Slack-HubSpot-ReEngage.git
cd Slack-HubSpot-ReEngage
```

2. Create a virtual environment
   
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies
   
``` pip install -r requirements.txt ```

5.	Configure environment variables

Create a .env file or export environment variables:

```bash
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_SIGNING_SECRET=your-slack-signing-secret
HUBSPOT_API_KEY=your-hubspot-developer-access-key
```
