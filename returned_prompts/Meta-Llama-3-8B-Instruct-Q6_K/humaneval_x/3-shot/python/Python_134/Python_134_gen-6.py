    txt = txt.strip()  # Remove leading and trailing spaces
    if len(txt) == 0:  # If the string is empty
        return False
    last_char = txt[-1]  # Get the last character
    if not last_char.isalpha():  # If the last character is not an alphabetical character
        return False
    if txt[-2:].isspace():  # If the last two characters are a space
        return False
    return True
