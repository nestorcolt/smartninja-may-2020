import json

# JSON AND API
##############################################################################################
"""
    Resources:
        https://docs.python.org/3/library/json.html
        https://realpython.com/python-json/

"""

# Load json (Means: Load the info from the JSON file into the program)
# json.load()

with open("people.json") as file:
    data = json.load(file)

for item in data:
    # print(item["id"], item["SSN"])
    pass

##############################################################################################
# Dump json (Means: Store the info in the json file)

"""

with open("people_2.json", "w") as writer:
    new_data = json.dumps(data, separators=(',', ':'), indent=4)
    print(type(new_data))
    writer.write(new_data)

with open("people_3.json", "w") as writer:
    json.dump(data, fp=writer, separators=(',', ':'), indent=4)

"""
