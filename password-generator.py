import string
import random


def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True,
                      include_special=True):
    characters = ''

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        print("Please include at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()