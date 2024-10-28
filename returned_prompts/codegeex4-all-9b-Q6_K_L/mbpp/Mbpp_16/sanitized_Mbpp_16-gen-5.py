def text_lowercase_underscore(text):
    """
    Check if the input string contains sequences of lowercase letters joined with an underscore.
    """
    # Split the string into substrings using underscore as the delimiter
    substrings = text.split('_')
    
    # Check if all substrings are lowercase letters
    for substring in substrings:
        if not substring.islower():
            return False
    
    return True