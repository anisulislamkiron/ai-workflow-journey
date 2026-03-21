age = 20

has_student_card = True

if age >= 18:
    if has_student_card:
        print("Student ticket: $10")
    else:
        print("Adult ticket: $15")

elif age <= 12:
    print("Child ticket: $5")

elif 13 <= age <= 17:
    print("Teen ticket: $8")