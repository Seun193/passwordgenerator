import random

def generate_password(length: int) -> str:
    # Characters to include in the password
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_xters = "$€<>!@#%^&*_=+-/.?)"

    passwd_xters = upper_case + lower_case + numbers + special_xters
    password = ""

    # Generate random characters for the password
    for i in range(length):
        password += random.choice(passwd_xters)

    return password

def main():
    length = 10  # Password length
    print("Your password:", generate_password(length))

if __name__ == "__main__":
    main()
