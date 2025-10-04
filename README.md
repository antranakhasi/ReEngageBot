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

```bash
ReEngageBot/  
├── app.py           # Starts the bot and ngrok tunnel 
├── hubspot.py       # HubSpot API integration (search deals, create tasks) 
├── slack.py         # Slack command handler (/reengage) 
├── config.py        # Loads Slack & HubSpot credentials from environment 
├── requirements.txt # Python dependencies 
└── README.md        # This file
```

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

---

## 5. Configure Slack

1. Go to Slack API: Your Apps and create a new app.  
2. Add a Slash Command `/reengage`:  
   - Request URL: `https://<your-ngrok-or-server-url>/slack/events`  
   - Method: POST  
3. Enable Event Subscriptions (optional):  
   - Request URL: same as above  
4. Install the app to your workspace.  
5. Make sure your bot has permissions to post messages in the channels where it will be used.  

---

## 6. Configure HubSpot

1. Go to your HubSpot Developer account and create a new app.  
2. Note the **Client ID**, **Client Secret**, or generate a **Private App API key**.  
3. Assign the necessary scopes to the app
4. Test your key or app credentials with a simple API call to confirm it works.  
5. The bot will:  
   - Search deals by a specific property and value.  
   - Create a task for each deal owner.  
   - Associate tasks back to the original deal.

---

## 7. Run Locally

1. Activate your virtual environment if not already active:

```bash
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

2.	Start the bot:

```bash
python app.py
```

3. 	If using ngrok, the script will print a public URL. Set this URL in Slack as your Request URL.

4. 	Test the Slack command in your workspace:

`/reengage <property_name> <property_value>`

Example: `/reengage product_interest "New Feature A"`

---

## 8. Usage

- Slack users can re-engage deals in HubSpot by running the `/reengage` command.  
- Supports multi-word property values.  
- Responses in Slack include:  
  - Number of tasks created.  
  - Errors (if any deals have no owner or fail to create a task).  

---

## 9. Deployment

- For production, deploy on a server (e.g., Heroku, AWS, Google Cloud) instead of ngrok.  
- Set environment variables on your deployment platform.  
- Ensure HTTPS endpoint for Slack commands (Slack requires a secure URL).  
- The bot will continue to create tasks for HubSpot deals without manual intervention.  

---

## 10. Troubleshooting

- `401 Unauthorized`: Check your HubSpot API key or Private App key and scopes.  
- No tasks created: Ensure the deals have a valid owner (`hubspot_owner_id`).  
- Multi-word property values not working: Always wrap them in quotes in Slack, e.g., `"New Feature A"`.  
- ngrok issues: Ensure your ngrok account is verified and authtoken installed.  
- Errors in Slack logs: Review your terminal where `app.py` is running for Python exceptions.  
