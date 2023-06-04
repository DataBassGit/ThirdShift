import os

# Salesforce API credentials
CLIENT_ID = os.environ.get("SALESFORCE_CONSUMER_KEY")
CLIENT_SECRET = os.environ.get("SALESFORCE_CONSUMER_SECRET")
USERNAME = os.environ.get("SALESFORCE_USERNAME")
PASSWORD = os.environ.get("SALESFORCE_PASSWORD")
SECURITY_TOKEN = os.environ.get("SALESFORCE_SECURITY_TOKEN")

# Salesforce API URLs
AUTH_URL = "https://login.salesforce.com/services/oauth2/token"
API_VERSION = "v52.0"