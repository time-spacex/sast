import subprocess

def vulnerable_function(user_input):
    # Command Injection vulnerability
    subprocess.run(f"ls {user_input}", shell=True)

def safe_function():
    print("This is a safe function")

vulnerable_function("example")
