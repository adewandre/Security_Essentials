import hashlib

# Function to read the rainbow table file and store hashes and passwords in a dictionary
def read_rainbow_table(file_name):
    rainbow_table = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:  # Make sure the line has at least two parts (hash value and password)
                hash_value = parts[0]
                password = " ".join(parts[1:])
                rainbow_table[hash_value] = password
            else:
                print(f"Invalid line in rainbow table: {line}")
    return rainbow_table


# Function to crack hashes using the rainbow table
def crack_hashes(hash_file, rainbow_table):
    cracked_passwords = {}
    with open(hash_file, 'r') as file:
        for line in file:
            hash_value = line.strip()
            if hash_value in rainbow_table:
                cracked_passwords[hash_value] = rainbow_table[hash_value]
            else:
                cracked_passwords[hash_value] = "Password not found in rainbow table"
    return cracked_passwords

# Main function
def main():
    # Input files
    hash_file = "sample_hashes.txt"
    rainbow_table_file = "md5woordenlijst.txt"

    # Read rainbow table
    rainbow_table = read_rainbow_table(rainbow_table_file)

    # Crack hashes
    cracked_passwords = crack_hashes(hash_file, rainbow_table)

    # Output results
    print("\nCracked Passwords:")
    for hash_value, password in cracked_passwords.items():
        print(f"Hash: {hash_value} - Password: {password}")

if __name__ == "__main__":
    main()
