import os
import requests
from dotenv import load_dotenv

load_dotenv()

class SalesforceAPIClient:
    print("Salesforce API Client:")
    def __init__(self, access_token=os.getenv("SALESFORCE_SECURITY_TOKEN"), instance_url=os.getenv("SALESFORCE_URL")):
        self.access_token = access_token
        self.instance_url = instance_url
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def api_request(self, endpoint, method="GET", data=None):
        print(f"{method} {endpoint}")
        url = f"{self.instance_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def get_access_token(self):
        print("- Getting access token.")
        return self.access_token

    def set_access_token(self, access_token):
        print(f"- Setting access token: {access_token}")
        self.access_token = access_token
        self.headers["Authorization"] = f"Bearer {self.access_token}"

    def refresh_token(self, refresh_token):
        # Implement refresh token logic here if needed
        pass