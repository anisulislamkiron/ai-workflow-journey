students = {
    "s001": {"name": "Arif", "grade": "A"},
    "s002": {"name": "Ron", "grade": "B"},
}


# print(students["s001"]["grade"])
# print(students["s002"]["name"])


# Safely with .get()
# print(students.get("s099", {}).get("name", "Not Found"))

# print(students.get("key", "default"))

print(students.items())