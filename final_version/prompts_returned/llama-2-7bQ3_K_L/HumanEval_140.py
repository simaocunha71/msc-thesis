
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    
    # Split the string into a list of characters, to make iteration easier
    chars = text.split()
        
    # Iterate through each letter in the string
    for character in chars:
        if len(character) > 1 and character[0] == ' ':
            print("Found ", character, " Replaced by -")
            
            # Replace all spaces with underscores
            character = "-" + character[1:]
        
    return ''.join(chars)
        