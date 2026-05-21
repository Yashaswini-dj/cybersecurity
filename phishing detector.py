email = input("Paste email message:")

suspicious_words = ["urgent", "immediately", "password", "account", "verify", "click here"] 

found = False

for word in suspicious_words:
    if word.lower() in email.lower():
        print(f"Suspicious word found: {word}")
        found = True

if  found:
    print("Possible phishing email")
else:
    print("Looks safer")