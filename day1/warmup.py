import requests

# Basic variables
username = input("Enter GitHub username: ")
url = f"https://api.github.com/users/{username}"


# Function example
def greet(person):
    return f"Hello, {person}! Welcome to Day 1."

# API request example
def fetch_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
    except Exception as e:
        print("Error:", e)

    return data["joke"]

# Run the functions
print(greet(username))
print("\nHere is your joke of the day:")
print(fetch_joke())
