def remove_uppercase(s):
    # Split the string into words
    words = s.split()

    # Initialize an empty string to store the modified string
    modified_string = ""

    # Iterate over each word in the string
    for word in words:
        # Check if the word contains any uppercase letters
        if not any(c.isupper() for c in word):
            # If the word does not contain any uppercase letters, append it to the modified string
            modified_string += word + " "
    
    # Remove the trailing whitespace and return the modified string
    return modified_string.strip()