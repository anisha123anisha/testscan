import os
import subprocess
import json

# Hardcoded secret - flagged by Bandit
SECRET_KEY = "supersecretpassword"

# Insecure eval usage - flagged by Bandit
def insecure_eval(user_input):
    result = eval(user_input)  # This is dangerous and should never be used with untrusted input
    print(f"Result: {result}")

# Insecure subprocess call - flagged by CodeQL and Bandit
def insecure_subprocess(command):
    # If the command contains user input, it could lead to arbitrary code execution
    subprocess.run(command, shell=True)

# Improper input validation - flagged by CodeQL
def process_data(data):
    try:
        # Dangerous: no validation of input, allowing for code injection or other attacks
        result = json.loads(data)  # This will succeed even with malicious input
        print("Processed data:", result)
    except json.JSONDecodeError:
        print("Invalid data format")

# Example of using insecure eval and subprocess in an actual program
if __name__ == "__main__":
    user_input = input("Enter a Python expression to evaluate: ")
    insecure_eval(user_input)

    user_command = input("Enter a shell command to run: ")
    insecure_subprocess(user_command)

    # Simulating JSON input with potential attack
    json_data = '{"user": "admin", "password": "password123"}'
    process_data(json_data)
