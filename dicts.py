# словари

import json
import pprint

d = {
    "key": "value",
    "another": "another value"
}

user1 = {"name": "Vasya",
         "age": 18,
         "id": 25
         }

user2 = {"name": "Petya",
         "age": 20,
         }

users = {
    25: user1,
    42: user2
}

print(users[42])

print(user1["name"])
print(user2["age"])

#users.pop(42)
#users.values(42)
#users.items(42)
#users.keys(42)
#print(users[42])
print(users.get(42, {"name": "default user"}))

users[55] = {"name": "Oleg", "age": 44}

from pprint import pprint

pprint(list(users.items()))