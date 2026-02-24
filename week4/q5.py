import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length Check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        remarks.append("Too short (aim for 12+ chars)")

    # Complexity Checks
    if re.search(r"[A-Z]", password): strength += 1
    else: remarks.append("Missing uppercase letter")

    if re.search(r"[a-z]", password): strength += 1
    else: remarks.append("Missing lowercase letter")

    if re.search(r"\d", password): strength += 1
    else: remarks.append("Missing numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): strength += 1
    else: remarks.append("Missing special characters")

    # Evaluation
    if strength >= 5:
        return "Strong", remarks
    elif 3 <= strength < 5:
        return "Moderate", remarks
    else:
        return "Weak", remarks

# Testing
test_passwords = ["123456", "Password123", "Stro#ngP@ss2024!"]
for p in test_passwords:
    rating, notes = check_password_strength(p)
    print(f"Password: {p} | Rating: {rating} | Suggestions: {notes}")