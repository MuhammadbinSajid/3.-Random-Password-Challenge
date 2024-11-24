import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."
    
    # Create lists of characters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    
    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    
    # Fill the rest of the password length with random characters
    all_characters = lowercase + uppercase + digits
    password += random.choices(all_characters, k=length - 3)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Convert list to string and return
    return ''.join(password)

# Example usage
password_length = int(input("Enter the desired password length: "))
print("Generated password:", generate_password(password_length))
