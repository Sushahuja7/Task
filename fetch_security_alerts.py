import os
import requests

# 🔹 GitHub Repository Details
OWNER = "Sushahuja7"
REPO = "Task"

# ✅ Fetch TOKEN securely from environment variables
TOKEN = os.getenv("TOKEN")

# ❌ Error if TOKEN is missing
if not TOKEN:
    raise ValueError("❌ ERROR: GitHub Token is missing! Set 'TOKEN' as an environment variable.")

# 🔹 GitHub API URL for Code Scanning Alerts
GITHUB_API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/code-scanning/alerts"

# 🔹 Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

# 🔹 Fetch alerts
def fetch_high_severity_alerts():
    response = requests.get(GITHUB_API_URL, headers=HEADERS)
    
    if response.status_code == 200:
        alerts = response.json()
        high_severity_alerts = [
            alert for alert in alerts if alert.get("rule", {}).get("security_severity_level") in ["high", "critical"]
        ]

        if high_severity_alerts:
            print("\n🔴 High/Critical Severity Alerts Found:\n")
            for alert in high_severity_alerts:
                print(f"📌 {alert['rule']['description']}")
                print(f"🔗 {alert['html_url']}")
                print(f"🛠️ Severity: {alert['rule']['security_severity_level'].upper()}\n")
        else:
            print("\n✅ No High or Critical severity alerts found!\n")

    else:
        print(f"❌ Failed to fetch alerts! Status Code: {response.status_code}")
        print(f"Response: {response.text}")

# Run the function
fetch_high_severity_alerts()
