# import json module
import json


# Load the username if it has been store previously.
# Otherwise prompt the username and store it.

# store the user name in a variable
filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)

except FileNotFoundError:
    # store the data in a json call username.
    username = input("What's your name: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")

else:
    print(f"Welcome back {username}!")