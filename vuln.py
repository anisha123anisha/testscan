import subprocess

def execute_command():
    # Critical vulnerability: User input directly passed to shell command
    user_input = input("Enter a command to execute: ")
    subprocess.call(f"echo {user_input}", shell=True)  # Dangerous use of shell=True

if __name__ == "__main__":
    execute_command()
