import os
import subprocess
import hashlib

# Example 1: Command Injection
def run_system_command(user_input):
    # This is vulnerable to command injection
    os.system(f"echo {user_input}")

# Example 2: Insecure Hashing (MD5)
def generate_md5_hash(password):
    # MD5 is not secure for hashing passwords
    return hashlib.md5(password.encode()).hexdigest()

# Example 3: Hardcoded Sensitive Information
def hardcoded_credentials():
    # Hardcoded password in the code (a common vulnerability)
    password = "mysecretpassword"
    return password

# Example 4: Insecure subprocess call (command injection risk)
def insecure_subprocess():
    user_input = "malicious_input; rm -rf /"  # Example of user input with a malicious command
    subprocess.run(f"ls {user_input}", shell=True)

# Example 5: Use of eval() (code injection risk)
def eval_example(user_input):
    # Evaluating user input is dangerous (code injection)
    result = eval(user_input)
    return result
