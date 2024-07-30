import string
import secrets
import os

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation + ' \t\n'
    return ''.join(secrets.choice(characters) for _ in range(length))

def get_integer_input(prompt, default):
    while True:
        try:
            value = input(prompt) or default
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no', 'y', 'n']:
            return response in ['yes', 'y']
        print("Invalid input. Please enter 'yes' or 'no'.\n")

def main():
    print("CSWC's Monkey Typewriter\n")
    try:
        length = get_integer_input("String length (default: 5,300,000 characters, approximate length of the complete works of William Shakespeare): ", 5300000)
        random_string = generate_random_string(length)
        
        save_to_file = get_yes_no_input("Would you like to save the generated string to a file? (yes/no): ")
        if save_to_file:
            filename = os.path.join(os.getcwd(), 'shakespeare.txt')
            with open(filename, 'w') as f:
                f.write(random_string)
            print(f"Generated random string of length {length}. Written to '{filename}'.")
        else:
            print(f"Generated random string: {random_string}")
            
    except KeyboardInterrupt:
        print(f"\nProcess interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()