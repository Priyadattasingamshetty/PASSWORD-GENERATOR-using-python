import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main function to run the password generator
def password_generator():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            
            if length < 1:
                print("Please enter a positive integer for the length.")
                continue

            password = generate_password(length)
            print(f"Generated password: {password}")

            cont = input("Do you want to generate another password? (yes/no): ").lower()
            if cont != 'yes':
                print("Thanks for using the password generator!")
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the length.")

# Start the password generator
password_generator()
