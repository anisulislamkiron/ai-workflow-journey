weight = float(input("Enter your weight in kg: "))

height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("BMI is under weight")
elif 18.5 <= bmi <= 24.9:
    print("BMI is Healthy weight")
elif 25.0 <= bmi <= 29.9:
    print("BMI is Over weight")
elif bmi > 30.0:
    print("BMI is Obesity")


print(f"Based on your weight {weight} kg and height {height} meters")

print(f"Your BMI is: {bmi:.2f}.")