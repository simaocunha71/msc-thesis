"""
Here is a simple solution using Python:

def text_lowercase_underscore(s):
    # Split the string into words
    words = s.split('_')

    # Check if all words are lowercase
    return all(word.islower() for word in words)

# Test the function
print(text_lowercase_underscore("aab_cbbbc")) # Should print True
"""

