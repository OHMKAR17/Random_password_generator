import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("=================================")
print("      RANDOM PASSWORD GENERATOR")
print("=================================")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length must be at least 4.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")
    
    