import json 

filename = 'userage.json'

try:
    with open(filename) as f:
        username_age = json.load(f)

except FileNotFoundError:
    with open(filename, 'w') as f:
        username_age = input("What's your name and age: ")
        json.dump(username_age, f)
        print(f"We'll remember you name and age when you come back. {username_age} years old.!")

else:
    print(f"Welcome back {username_age} years old.")
