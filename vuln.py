import os

# Vulnerable code: Command injection via user input
user_input = input("Enter a file name to display its contents: ")

# Dangerous system call that directly uses user input
os.system(f"cat {user_input}")
