
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False

    last_char = txt[-1]
    if not last_char.isalpha():
        return False

    if txt.count(last_char) > 1:
        return False

    return True


# Tests
print(check_if_last_char_is_a_letter("apple pie"))  # False
print(check_if_last_char_is_a_letter("apple pi e"))  # True
print(check_if_last_char_is_a_letter("apple pi e "))  # False
print(check_if_last_char_is_a_letter(""))  # False






def check_if_last_char_is_a_letter(txt):
    # If the length of the text is 0, return False
    if len(txt) == 0:
        return False

    # Get the last character of the text
    last_char = txt[-1]

    # If the last character is not alphabetical, return False
    if not last_char.isalpha():
        return False

    # Get the count of the last character in the text
    count = txt.count(last_char)

    # If the count of the last character is greater than 1, return False
    if count > 1:
        return False

    # Otherwise, return True
    return True

# Test cases
print(check_if_last_char_is_a_letter("apple pie"))  # False
print(check_if_last_char_is_a_letter("apple pi e"))  # True
print(check_if_last_char_is_a_letter("apple pi e "))  # False
print(check_if_last_char_is_a_letter(""))  # False






def check_if_last_char_is_a_letter(txt):
    # Check if the length of the text is 0
    if len(txt) == 0:
        return False

    # Get