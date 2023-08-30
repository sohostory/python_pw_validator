import re

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")

password = input("Enter your password: ")
isValid = pattern.fullmatch(password)

if isValid:
    print("Password is valid.")
else:
    print("Password is not valid.")
