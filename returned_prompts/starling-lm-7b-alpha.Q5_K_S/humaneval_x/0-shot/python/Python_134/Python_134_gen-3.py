
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    if txt[-1].isalpha():
        return True
    if ' ' in txt[:-1]:
        return False
    return True

# Tests
print(check_if_last_char_is_a_letter("apple pie"))  # False
print(check_if_last_char_is_a_letter("apple pi e"))  # True
print(check_if_last_char_is_a_letter("apple pi e "))  # False
print(check_if_last_char_is_a_letter(""))  # False




def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    if txt[-1].isalpha():
        return True
    if ' ' in txt[:-1]:
        return False
    return True

# Tests
print(check_if_last_char_is_a_letter("apple pie"))  # False
print(check_if_last_char_is_a_letter("apple pi e"))  # True
print(check_if_last_char_is_a_letter("apple pi e "))  # False
print(check_if_last_char_is_a_letter(""))  # False


# Here's a step-by-step explanation of the code:

# First, we check if the length of the given string is 0. If it is, this means there are no characters in the string, so we return False.

# Next, we check if the last character of the string is an alphabetical character using the `isalpha()` method. If it is, we return True, as this means the last character is a letter and not part of a word.

# If the last character is not an alphabetical character, we then check if there is a space character in the string before the last character. If there is, this means the last character is part of a word, so we return False.

# If neither of the above conditions are met, this means the last character is an alphabetical