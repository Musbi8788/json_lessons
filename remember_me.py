# import json module
import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new user"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    
    if username:
        verify_user = input(f"Is this your name {username}, type(yes/no) ")
        if verify_user.lower() == 'yes':
            print(f"Welcome back {username}!")
        elif verify_user.lower() == 'no' :
            username = get_new_username()
            print(f"We'll remember you when you are back, {username}!")
        else:
            print("Please type 'yes' or 'no'")

    else:
        username = get_new_username()
        print(f"I'll remember you when you come back {username}!")


greet_user()