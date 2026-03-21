score = float(input("Enter your score: "))

if score > 100:
    print("Wrong Input")

elif score >= 80:
    print("Grade A")
    print("Best output")

elif score >= 70:
    print("Grade B")
    print("Good Job")

elif score >= 60:
    print("Grade C")
    print("Nice try")

elif score >= 50:
    print("Grade D")
    print("You passed, but work harder")

else:
    print("Fail")
    print("Try again")