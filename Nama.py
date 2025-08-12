# Hardcoded password
PASSWORD = "MySecret123"

# Ask user for password
user_input = input("Enter password: ")

# Check password
if user_input == PASSWORD:
    print("Access granted")
else:
    print("Access denied")
