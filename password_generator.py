#!/usr/bin/env python3

import secrets
import string
import argparse

def generate_secure_password(length=32):
    if length < 4:
        raise ValueError("La longitud de la contraseña debe ser al menos 4 para incluir todos los tipos de caracteres.")
    
    # Define the character sets for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    # Ensure the password includes at least one character from each set
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]
    
    # Fill the rest of the password length with a random selection of all characters
    all_characters = lowercase + uppercase + digits + punctuation
    password += [secrets.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffle the resulting password to avoid any predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password")
    parser.add_argument('-l', '--length', type=int, default=32, help="Length of the password (default: 32)")
    args = parser.parse_args()

    password = generate_secure_password(args.length)
    print(f"Generated secure password: {password}")

if __name__ == "__main__":
    main()
