import subprocess
import hashlib

def insecure_command(cmd):
    subprocess.call(cmd, shell=True)  # Critical vulnerability: Arbitrary command execution

def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()  # Weak MD5 hashing algorithm

if __name__ == "__main__":
    insecure_command("ls -l")
    print("Password hash:", weak_hash("password123")) #test
