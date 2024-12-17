import os
import hashlib

# Vulnerability 1: Command Injection
def list_directory(user_input):
    # Directly passing user input to os.system (command injection risk)
    os.system(f"ls {user_input}")

# Vulnerability 2: Hardcoded Credentials
def connect_to_service():
    # Hardcoded sensitive information
    username = "admin"
    password = "12345"  # Hardcoded weak password
    print(f"Connecting to service with username: {username} and password: {password}")

# Vulnerability 3: Insecure Hashing Algorithm
def hash_password(password):
    # Using insecure hashing algorithm (MD5)
    hashed = hashlib.md5(password.encode()).hexdigest()
    print(f"MD5 hash of the password is: {hashed}")

# Main function to demonstrate vulnerabilities
if __name__ == "__main__":
    # Example input to trigger vulnerabilities
    user_input = input("Enter directory name: ")  # User input for command injection
    list_directory(user_input)

    # Hardcoded credentials being used
    connect_to_service()

    # Weak hash usage
    password = input("Enter a password to hash: ")
    hash_password(password)
