import json

numbers = [3, 6, 8, 11, 23, 34]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)