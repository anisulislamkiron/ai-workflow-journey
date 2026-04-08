# Just ask yourself: "do I have a colon?" No colon = not a dictionary comprehension.

names = ["ali", "sara", "john"]
result = {name.upper(): len(name) for name in names}

# print(result)  # {"ALI": 3, "SARA": 4, "JOHN": 4}

students = {"ali": 40, "sara": 75, "john": 55, "mia": 90}

# So student gives you just the name (the key), not the score.
# To get the score (value), you write students[student] — just like you did earlier with prices[item]!
marks = {student: students[student] for student in students if students[student] >= 60}
print(marks)

