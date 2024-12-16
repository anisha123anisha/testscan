import subprocess
import hashlib

# --- 1. CRITICAL: Use of subprocess with user-controlled input ---
def execute_command(user_input):
    # CRITICAL: Dangerous use of subprocess with user-controlled input
    subprocess.call(f"echo {user_input}", shell=True)

# --- 2. HIGH: Hardcoded password in the code ---
def connect_to_service():
    # HIGH: Hardcoded password in plain text
    password = "super_secret_password123"
    print("Connecting to service with password:", password)

# --- 3. LOW: Use of assert statements for security checks ---
def check_user_permission(user):
    # LOW: Use of assert for security check
    assert user.is_admin, "User must be an admin to access this function"
    print("Admin access granted!")

class User:
    def __init__(self, is_admin):
        self.is_admin = is_admin

# --- 4. LOW: Use of insecure hashing algorithm (MD5) ---
def hash_password(password):
    # LOW: Use of insecure MD5 hash
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed

# --- MAIN PROGRAM ---
if __name__ == "__main__":
    # 1. CRITICAL: Subprocess with user input
    print("1. CRITICAL: Subprocess Command Injection Example")
    user_input = input("Enter a command to execute: ")
    execute_command(user_input)

    # 2. HIGH: Hardcoded password
    print("\n2. HIGH: Hardcoded Password Example")
    connect_to_service()

    # 3. LOW: Assert statement for security check
    print("\n3. LOW: Assert Statement Example")
    user = User(is_admin=False)  # Simulating a non-admin user
    try:
        check_user_permission(user)
    except AssertionError as e:
        print("Error:", e)

    # 4. LOW: Insecure Hashing Example
    print("\n4. LOW: Insecure MD5 Hash Example")
    password = "my_password"
    hashed_password = hash_password(password)
    print("Hashed password (MD5):", hashed_password)
