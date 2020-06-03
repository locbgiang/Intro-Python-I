# Dictionaries are Python's version of Objects in JS 
# Useful for storing key-value pairs 
​
# init an empty dict
d = {}
​
# create a dict with two key-value pairs 
e = {"foo": 12, 16: "bar"}
​
# note for JS users: there's no dot notation for accessing
# values in dicts in Python 
# print(e["foo"])
# print(e[16])
​
# loop through keys in dicts option 1:
# for key in e:
#     # print out both the key and the value 
#     print(key, e[key])
​
# loop through keys and values option 2:
for key, val in e.items():
    print(key, val)