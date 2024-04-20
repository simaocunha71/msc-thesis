"""
Write a function to count the total number of characters in a string.
assert count_charac("python programming")==18
"""

def count_character(string):
    """
        Returns the char length of a given string
    """
    # Your Solution Below
    return len([c for c in string if c])