import os
import json
import hashlib
import getpass  # For secure password input

# Store user data in a JSON file (simple, but not ideal for large-scale)
USER_DATA_FILE = "users.json"

def load_user_data():
    """Load user data from the JSON file.  Handles file not found and JSON decode errors."""
    try:
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No existing user database found, creating a new one.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON.  The user database file may be corrupted.  Returning an empty database.")
        return {}  # Return an empty dict to avoid crashing, but consider more robust error handling

def save_user_data(data):
    """Save user data to the JSON file."""
    try:
        with open(USER_DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)  # Use indent for human-readable formatting
    except Exception as e:
        print(f"An error occurred while saving user data: {e}")
        # Consider more robust error handling (e.g., logging, retrying)

def hash_password(password):
    """Hash the password using SHA-256.  Salting is important for security, but we'll keep it simple here."""
    return hashlib.sha256(password.encode()).hexdigest()

def create_user():
    """Create a new user account."""
    username = input("Enter username: ")
    if not username.strip():
        print("Username cannot be empty.")
        return

    users = load_user_data()
    if username in users:
        print("Username already exists.")
        return

    # Use getpass.getpass() for secure password entry
    password = getpass.getpass("Enter password: ")
    if not password.strip():
        print("Password cannot be empty.")
        return
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match.")
        return

    hashed_password = hash_password(password)  # Hash the password
    users[username] = {"password": hashed_password, "role": "user"}  # Store hashed password and default role.
    save_user_data(users)
    print("User created successfully.")

def login_user():
    """Log in an existing user."""
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    users = load_user_data()
    if username not in users:
        print("Invalid username.")
        return

    hashed_password = hash_password(password)
    if users[username]["password"] != hashed_password:
        print("Invalid password.")
        return

    print(f"Logged in as {username}.  Role: {users[username]['role']}")
    return username, users[username]['role'] # Return username and role

def display_dashboard(username, role):
    """Display the user dashboard.  The content depends on the user's role."""
    print("\n--- User Dashboard ---")
    print(f"Welcome, {username}!")
    print(f"Your role: {role}")

    if role == "admin":
        print("1. View all users")  # Example admin-only action
        print("2. Manage system settings") #Another Example
        print("3. Generate Report")
    elif role == "user":
        print("1. View your profile")
        print("2. Change your password")
        print("3. View Game Stats")
    else:
        print("Invalid role.") #Should never happen, unless data is corrupt

def view_all_users():
    """View all users (admin only)."""
    users = load_user_data()
    print("\n--- All Users ---")
    for username, data in users.items():
        print(f"Username: {username}, Role: {data['role']}")

def change_password(username):
    """Change the user's password"""
    users = load_user_data()
    password = getpass.getpass("Enter your current password: ")
    hashed_password = hash_password(password)

    if users[username]["password"] != hashed_password:
        print("Incorrect password")
        return

    new_password = getpass.getpass("Enter your new password: ")
    if not new_password.strip():
        print("New Password cannot be empty")
        return

    confirm_new_password = getpass.getpass("Confirm your new password: ")

    if new_password != confirm_new_password:
        print("New passwords do not match")
        return

    users[username]["password"] = hash_password(new_password)
    save_user_data(users)
    print("Password changed successfully")

def main():
    """Main function to run the program."""
    while True:
        print("\n--- User Login System ---")
        print("1. Create User")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            user_info = login_user() #changed from username, role
            if user_info:
                username, role = user_info #unpack user info
                display_dashboard(username, role)
                if role == "admin":
                  admin_choice = input("Enter your choice: ")
                  if admin_choice == "1":
                    view_all_users()
                elif role == "user":
                    user_choice = input("Enter your choice: ")
                    if user_choice == "2":
                        change_password(username)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


