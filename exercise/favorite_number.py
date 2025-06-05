import json 

filename = 'favorite_number.json'

user_favorite_number = input("Enter your favorite number: ")
with open(filename, 'w') as f:
    json.dump(user_favorite_number, f)
    print(f"I'll remember your favorite number, {user_favorite_number}")