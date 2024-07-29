import os

# Function to register a new user
def register_user():
    print("Welcome to Event Registration!")
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")

    user_info = f"{name},{email},{phone}\n"

    # Append user info to the file
    with open('registered_users.txt', 'a') as file:
        file.write(user_info)

    print("Registration successful!\n")

# Function to display all registered users
def show_registered_users():
    if not os.path.exists('registered_users.txt'):
        print("No users registered yet.")
        return

    print("\nList of registered users:")
    with open('registered_users.txt', 'r') as file:
        for idx, line in enumerate(file, start=1):
            name, email, phone = line.strip().split(',')
            print(f"{idx}. Name: {name}, Email: {email}, Phone: {phone}")

    print()

# Main function to run the program
def main():
    while True:
        print("\nMenu:")
        print("1. Register for the event")
        print("2. Show registered users")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            register_user()
        elif choice == '2':
            show_registered_users()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
