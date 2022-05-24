import random
import string
from colorama import Fore, Back, Style

#Function to generate a random password
def generate_random_password(length):
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password)

#Line 16 can be edited based on where you want passwords.txt to be created. This will create it right where the program is stored.
with open("passwords.txt", "at") as e:
    option = input("\nDo you want to\n"
                              "(E)xtract credentials or\n"
                              "(C)reate new credentials?\n"
                              "> ").upper()

    if option == "C":

        website_name = input("Website Name: ")
        check = input("Confirm Website Name: ")
        while check != website_name and check == " ":
            website_name = input("re-enter Website Name: ")
            check = input("re-enter Confirmation: ")

        username = input("Enter the Username: ")
        password_length = int(input("Enter password length in digits: "))

        new_password = generate_random_password(password_length)
        print(website_name + "   |   " + username + "   |   " + new_password + "\n")
        e.write(website_name + "   |   " + username + "   |   " + new_password + "\n")
        e.close()

    elif option == "E":
        Website_Name = input("Enter name of Website for credentials: ")
        Username = input("Enter name of Username: ")
        f = open("passwords.txt", "r+")
        line_check = 0
        lines = 0
        for i in f:
            lines +=1
            Rule = Website_Name + "   |   " + Username
            if Rule not in i:
                line_check +=1
            else:
                separator_index = i.find("|")
                i = list(i)
                i.pop(separator_index)
                i = "".join(i)
                separator_index = i.find("|")
                print(f"\nUser: {Username}" +
                      f"\nWebsite: {Website_Name}" +
                      #f"\nPassword: \033[1;31;40m{i[separator_index+4:-1]}\n"
                      f"\nPassword: {Fore.RED}{i[separator_index+4:-1]}{Style.RESET_ALL}\n")
        if line_check == lines:
            print("No Record of Credentials for this Website.")
