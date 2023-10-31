import random
import string

def generate_password(length):
    # Define the character pool for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by selecting random characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
