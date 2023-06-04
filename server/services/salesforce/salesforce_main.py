import os
import requests
from services.salesforce.salesforce_api_client import SalesforceAPIClient
from dotenv import load_dotenv

load_dotenv()

class SalesforceMain():
    def __init__(self):
        self.sales_force=SalesforceAPIClient(access_token=os.environ.get("SALESFORCE_SECURITY_TOKEN"), instance_url=os.environ.get("SALESFORCE_URL"))

    def main(self):
        print("Sales Force Main:")
        access_token = self.sales_force.getAccessToken()
        instance_url = "https://agentforge2-dev-ed.develop.lightning.force.com/"
        self.get_user_info(
            instance_url,
            access_token,
            "/services/data/v52.0/query?q=SELECT+Name+FROM+User",
            "User information:",
        )
        if new_access_token := self.sales_force.refreshToken():
            access_token = new_access_token

        self.get_user_info(
            instance_url,
            access_token,
            "/services/data/v52.0/query?q=SELECT+Name+FROM+Account",
            "Account information:",
        )
    def get_user_info(self, access_token, user_id):
        print("- Getting access token.")
        # Example API request to get user information
        endpoint = f"{self}/services/data/v52.0/sobjects/User/{user_id}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(endpoint, headers=headers)

        # TODO: Handle response status codes and possible exceptions
        response.raise_for_status()

        return response.json()
