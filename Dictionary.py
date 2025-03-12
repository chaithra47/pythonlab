# dictionary creation
student = { 
    "name": "John",
    "age": 20,
    "course": "python"
}

# accessing values
print("Name: ", student["name"])

# adding a new key-value pair
student["grade"] = "A"

# updating a value
student["age"] = 21

# deleting a key-value pair
del student["course"]

print("Upadated dictionary: ", student)