the app is: Simple REST API client for Salesforce API

the files we have decided to generate are: salesforce_api_client.js, index.html

Shared dependencies:
1. access_token: OAuth token used to request access to protected resources.
2. id: Identity URL to identify the user and query for more information.
3. instance_url: URL indicating the instance of the user's org.
4. issued_at: Timestamp of when the signature was created.
5. signature: Base64-encoded HMAC-SHA256 signature signed with the client_secret.
6. sfdc_community_url: URL of the Experience Cloud site.
7. sfdc_community_id: User's Experience Cloud site ID.
8. token_type: Bearer token type used for responses with an access token.
9. id_token: Signed data structure containing authenticated user attributes (returned if scope parameter includes openid).
10. refresh_token: Token obtained from the web server, user-agent, or hybrid app token flow (returned if the connected app is set up with a refresh_token scope).
11. state: State requested by the client (included only if the state parameter is included in the original query string).

Function names:
1. getAccessToken: Function to retrieve the access token.
2. apiRequest: Function to make API requests to Salesforce API.
3. refreshToken: Function to refresh the access token (if applicable).

X3rdShiftAssignLeads__c