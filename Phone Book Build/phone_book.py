phonebook = {}

def add_contact(phonebook, name, number):
    phonebook [name] = number
    print(f"{name} added")

def search_contact(phonebook, name):
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"{name} not found.")

def delete_contact (phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted.")

    else: 
        print(f"{name} not found.")

def display_all(phonebook):
    if phonebook:
        for name, number in phonebook.items():
            print(f"{name}: {number}")

    else:
        print("Phonebook is empty")

while True:
    print("\n1. Add  2. Search  3. Delete  4. Display  5. Quit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Number: ")
        add_contact (phonebook, name, number)

    elif choice == "2":
        name = input("Name to search: ")
        search_contact(phonebook, name)

    elif choice == "3":
        name = input ("Name to delete: ")

        delete_contact(phonebook, name)

    elif choice == "4":
        display_all(phonebook)

    elif choice == "5":
        break

    else:
        print("Invalid Choice.")