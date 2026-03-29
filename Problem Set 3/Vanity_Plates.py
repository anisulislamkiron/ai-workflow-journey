def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 2: Check length
    if not (2 <= len(s) <= 6):
        return False

    # Rule 1: Check if the first two characters are letters
    if not s[0:2].isalpha():
        return False

    # Rule 3, 4, & 5: Numbers and special characters
    i = 0
    while i < len(s):
        # Rule 5: Check for punctuation/spaces
        if not s[i].isalnum():
            return False
            
        # Rule 3 & 4: If we hit a number...
        if s[i].isdigit():
            # Rule 4: The first number cannot be '0'
            if s[i] == '0':
                return False
            
            # Rule 3: Once a number starts, everything after it MUST be a number
            if not s[i:].isdigit():
                return False
            
            # If we passed the "no zero" and "all numbers after" checks, we're good!
            break
            
        i += 1

    return True
     
main()