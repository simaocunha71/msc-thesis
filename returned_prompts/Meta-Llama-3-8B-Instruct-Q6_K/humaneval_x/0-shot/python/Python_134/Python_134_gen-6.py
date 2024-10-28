def check_if_last_char_is_a_letter(txt):
    txt = txt.strip() # Remove leading and trailing spaces
    if len(txt) == 0: # If the string is empty
        return False
    last_char = txt[-1] # Get the last character
    if last_char.isalpha(): # Check if the last character is an alphabetical character
        if txt.count(last_char) == 1: # Check if the last character is not part of a word
            return True
    return False
# Test the function
print(check_if_last_char_is_a_letter("apple pie")) # False
print(check_if_last_char_is_a_letter("apple pi e")) # True
print(check_if_last_char_is_a_letter("apple pi e ")) # False
print(check_if_last_char_is_a_letter("")) # False
print(check_if_last_char_is_a_letter("a")) # False
print(check_if_last_char_is_a_letter("a b")) # True
print(check_if_last_char_is_a_letter("abc")) # False
print(check_if_last_char_is_a_letter("ab c")) # True
print(check_if_last_char_is_a_letter("ab c ")) # False
print(check_if_last_char_is_a_letter("abcde")) # False
print(check_if_last_char_is_a_letter("abcde ")) # False
print(check_if_last_char_is_a_letter("abc de")) # True
print(check_if_last_char_is_a_letter("abc de ")) # False
print(check_if_last_char_is_a_letter("abc deeee")) # True
print(check_if_last_char_is_a_letter("abc deeee ")) # False
print(check_if_last_char_is_a_letter("a b c")) # False
print(check_if_last_char_is_a_letter("a b c ")) # False
print(check_if_last_char_is_a_letter("a b c d")) # False
print(check_if_last_char_is_a_letter("a b c d ")) # False
print(check_if_last_char_is_a_letter("a b c d e")) # False
print(check_if_last_char_is_a_letter("a b c d e ")) # False
print(check_if_last_char_is_a_letter("a b c d e f")) # False
print(check_if_last_char_is_a_letter("a b c d e f ")) # False
print(check_if_last_char_is_a_letter("a b c d e f g")) # False
print(check_if_last_char_is_a_letter("a b c d e f g