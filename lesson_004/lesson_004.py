# LIST AND DICTIONARIES

"""
Resources
    https://www.tutorialspoint.com/python/python_lists.htm
"""

##############################################################################################
# list
"""
some_list = [1, 34, 12, 17, 87]
# print(some_list)

another_list = ["tesla", "toyota", "nissan"]
# print(another_list)

mixed_list = [22, "elon", True, "SmartNinja", 3.14, [], [1, 2, 3, 4, ["un_string", "que"]]]
print(mixed_list)

# Indexing
# Getting the first element of mixed_list or the element in the index 0
print(mixed_list[0])

# Getting the second element of mixed_list or the element in the index 1
print(mixed_list[1])

# Negative indexing
print(mixed_list[-1])
print(mixed_list[-2])

# Getting an element inside of a nested list
print(mixed_list[-1][-1][0])

# Right way to do it
short_list = mixed_list[-1]
print(short_list[-1])

"""
##############################################################################################
"""
# Slicing
mixed_list = [22, "elon", True, "SmartNinja", 3.14, [], [1, 2, 3, 4, ["un_string", "que"]]]
# print(mixed_list[0:4])

# Methods of list
print(mixed_list)

# Append
mixed_list.append("un_gato")
print(mixed_list)

# Insert
mixed_list.insert(0, "una casa")

# Remove
mixed_list.remove(22)
print(mixed_list)

# Pop
popped_item = mixed_list.pop(-1)
print(popped_item)

# Query the length of a list
print(mixed_list)
print(len(mixed_list))

"""
##############################################################################################
# Dictionaries
"""
box = {"height": 20, "width": 45, "length": 30}
print(box)

# Pop dict
print(box.pop("height"))
print(box)

# print(box["new_key"]) # This one fails if not found
dict_check = box.get("new_key")

if dict_check is None:
    pass
    box["new_key"] = 99

print(box)
"""
##############################################################################################

