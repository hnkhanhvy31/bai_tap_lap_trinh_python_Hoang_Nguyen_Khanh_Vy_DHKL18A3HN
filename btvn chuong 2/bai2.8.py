import json

json_str = '''
[
  {"id": 1, "name": "An", "age": 20},
  {"id": 2, "name": "Bình", "age": 21}
]
'''

data = json.loads(json_str)

for item in data:
    print(item)