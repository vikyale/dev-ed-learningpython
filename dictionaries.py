user = {"name":"Vicky", "email":"vicky@gmail.com",
        "age":20,"purchases":[1,2,3,4]}

"""
user["name"] = 'Anna'
print(user)
"""

""""
print("\nItem: ")
for item in user:  
    print(item)

print("\nKey: ")
for key in user:
    print(key)


for key,val in user.items():
    print(key)
    print(val)
"""
"""
print(user.items())
"""
if "logged" in user:
    print('it is!')

del user["purchases"]

print(user)
