import re

password = input("Enter your password: ")

length = len(password)

has_upper = re.search(r"[A-Z]", password)
has_lower = re.search(r"[a-z]", password)
has_digit = re.search(r"[0-9]", password)
has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

score = 0

if length >=8:
    score += 1

if has_upper:
    score +=1

if has_lower:
    score +=1

if has_digit:
    score +=1

if has_special:
    score +=1

if score <= 2:
    print("weak Password")
elif score == 3 or score == 4:
    print("Medium Password")
else:
    print("strong password")