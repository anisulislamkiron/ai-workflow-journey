user_input = input("Input: ")

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

for char in user_input:
    if char not in vowels:
        print(char, sep="", end="")

print()