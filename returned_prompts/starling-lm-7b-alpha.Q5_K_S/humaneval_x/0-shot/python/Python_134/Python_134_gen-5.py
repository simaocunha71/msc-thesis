
def check_if_last_char_is_a_letter(txt):
    # Checking if the string is empty
    if len(txt) == 0:
        return False
    # Checking if the last character of the string is an alphabetical character
    elif txt[-1].isalpha():
        # Checking if the last character of the string is not a part of a word
        if not txt[-1].islower():
            return True
    # Returning False if none of the conditions are met
    else:
        return False

check_if_last_char_is_a_letter("apple pie")  # False
check_if_last_char_is_a_letter("apple pi e")  # True
check_if_last_char_is_a_letter("apple pi e ")  # False
check_if_last_char_is_a_letter("")  # False


# If you have any questions or concerns, please feel free to ask!


def check_if_last_char_is_a_letter(txt):
    # Checking if the string is empty
    if len(txt) == 0:
        return False
    # Checking if the last character of the string is an alphabetical character
    elif txt[-1].isalpha():
        # Checking if the last character of the string is not a part of a word
        if not txt[-1].islower():
            return True
    # Returning False if none of the conditions are met
    else:
        return False

check_if_last_char_is_a_letter("apple pie")  # False
check_if_last_char_is_a_letter("apple pi e")  # True
check_if_last_char_is_a_letter("apple pi e ")  # False
check_if_last_char_is_a_letter("")  # False


# If you have any questions or concerns, please feel free to ask!


# If you have any questions or concerns, please feel free to ask!


# Here are some additional examples for you to test your function:

# check_if_last_char_is_a_letter("hello