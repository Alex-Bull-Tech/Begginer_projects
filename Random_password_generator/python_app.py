import string
import random

characters = list(string.ascii_letters + string.digits + "!£$%^&(*")

def generate_password():
    password_lenght = int(input("How long woud you like the password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_lenght):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Do you want to generate a password?  (Yes/No): ")


if option == "Yes".lower():
    generate_password()
elif option == "No".lower():
    print("Program ended")
    quit()
else: 
    print("Invalid input, please input Yes or No")
    quit()

