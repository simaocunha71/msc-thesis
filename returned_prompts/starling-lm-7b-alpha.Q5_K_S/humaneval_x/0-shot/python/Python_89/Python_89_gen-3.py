
def encrypt(s):
    # Create a list of all lowercase and uppercase alphabets
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Create a list to store the encrypted alphabets
    encrypted_alphabet = ''

    # Iterate through each alphabet
    for c in alphabet:
        # If the alphabet is lowercase
        if c.islower():
            # Calculate the encrypted letter by adding the rotated value to the current letter
            encrypted_alphabet += chr(ord(c) + 2 * 2)
        # If the alphabet is uppercase
        elif c.isupper():
            # Calculate the encrypted letter by adding the rotated value to the current letter
            encrypted_alphabet += chr(ord(c) + 2 * 2 - 26)

    # Create a dictionary to store the mapping between the original and encrypted alphabets
    alphabet_mapping = {}
    # Iterate through each alphabet and add it to the dictionary
    for i in range(len(alphabet)):
        alphabet_mapping[alphabet[i]] = encrypted_alphabet[i]

    # Create a list to store the encrypted characters
    encrypted_string = ''
    # Iterate through each character in the input string
    for c in s:
        # Check if the character is an alphabet
        if c.isalpha():
            # Add the encrypted character to the list
            encrypted_string += alphabet_mapping[c.lower()]
        else:
            # If the character is not an alphabet, add it as it is
            encrypted_string += c

    return encrypted_string

# Test the function
print(encrypt('hi'))  # Output: lm
print(encrypt('asdfghjkl'))  # Output: ewhjklnop
print(encrypt('gf'))  # Output: kj
print(encrypt('et'))  # Output: ix

# Time complexity: O(n), where n is the length of the input string
