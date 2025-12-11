import requests

response = requests.get("https://api.github.com")

# Turn the response into Python data
data = response.json()

# Print somehthing interesting from the API
print("Current GitHub rate limit URL:", data["rate_limit_url"])