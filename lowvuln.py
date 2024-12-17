import os

# Low severity: Use of `os.system` for simple command execution
# Bandit considers it a low severity issue when the command is static.
def list_files():
    os.system("ls -la")  # Static command execution

# Main function to call the above method
if __name__ == "__main__":
    list_files()
