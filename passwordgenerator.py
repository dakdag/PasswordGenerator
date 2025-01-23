import random

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = "abcdefghijklmnopqrstuvwxyz"
    
    if use_uppercase == "yes":
        characters = characters + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if use_numbers == "yes":
        characters = characters + "0123456789"
    
    if use_special_chars == "yes":
        characters = characters + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    password = ""
    
    for i in range(length):
        random_character = random.choice(characters)
        password = password + random_character
    
    return password

print("Welcome to the password generator!")

length = int(input("How long do you want your password? (Enter a number): "))
use_uppercase = input("Do you want uppercase letters? (yes/no): ")
use_numbers = input("Do you want numbers in your password? (yes/no): ")
use_special_chars = input("Do you want special characters? (yes/no): ")

password = generate_password(length, use_uppercase, use_numbers, use_special_chars)

print("Your generated password is:", password)
