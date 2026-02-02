import re
# Email validation
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False
# Indian mobile number validation
def validate_mobile(mobile):
    pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
    if re.match(pattern, mobile):
        return True
    return False
# Password validation
def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(pattern, password):
        return True
    return False
def main():
    print("=== REGEX DATA VALIDATION ===")
    email = input("Enter Email: ").strip()
    mobile = input("Enter Mobile Number: ").strip()
    password = input("Enter Password: ").strip()
    # Edge case: empty input
    if not email or not mobile or not password:
        print(" Error: Input fields cannot be empty")
        return
    if validate_email(email):
        print(" Email is valid")
    else:
        print(" Invalid Email format")

    if validate_mobile(mobile):
        print(" Mobile number is valid")
    else:
        print(" Invalid Indian mobile number")

    if validate_password(password):
        print(" Password is strong")
    else:
        print(" Password must be 8+ chars, include upper, lower, digit & special char")

if __name__ == "__main__":
    main()
