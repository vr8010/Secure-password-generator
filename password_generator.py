import random
import string
import sys

def get_yes_no_input(prompt):
    """Get yes/no input from user."""
    while True:
        response = input(prompt).lower()
        if response in ['y', 'n', 'yes', 'no']:
            return response in ['y', 'yes']
        print("Please enter 'y' or 'n'")

def get_password_length():
    """Get and validate password length from user."""
    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 4:
                print("Password length should be at least 4 characters for security.")
                continue
            if length > 128:
                print("Password length should not exceed 128 characters.")
                continue
            return length
        except ValueError:
            print("Please enter a valid number.")

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    """Generate a random password based on specified criteria."""
    # Start with lowercase letters (always included)
    characters = string.ascii_lowercase
    
    # Build character set based on user preferences
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Ensure at least one character from each selected category
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    # Fill remaining length with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def main():
    """Main function to run the password generator."""
    print("=" * 40)
    print("=== Random Password Generator ===")
    print("=" * 40)
    print()
    
    try:
        # Get user preferences
        length = get_password_length()
        use_uppercase = get_yes_no_input("Include uppercase letters? (y/n): ")
        use_numbers = get_yes_no_input("Include numbers? (y/n): ")
        use_special = get_yes_no_input("Include special characters? (y/n): ")
        
        # Generate password
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        
        # Display result
        print()
        print("Generated Password:", password)
        print()



    
    except KeyboardInterrupt:
        print("\n\nPassword generation cancelled.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
