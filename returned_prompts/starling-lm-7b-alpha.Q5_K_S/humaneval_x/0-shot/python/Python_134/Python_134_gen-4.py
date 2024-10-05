
def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    if txt[-1].isalpha() and not txt[-1].islower() and not txt[-1].isupper():
        return True
    return False

# tests
print(check_if_last_char_is_a_letter("apple pie"))  # False
print(check_if_last_char_is_a_letter("apple pi e"))  # True
print(check_if_last_char_is_a_letter("apple pi e "))  # False
print(check_if_last_char_is_a_letter(""))  # False



# Alternative solution:
def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    return txt[-1].isalpha() and not txt[-1].islower() and not txt[-1].isupper()

# tests
print(check_if_last_char_is_a_letter("apple pie"))  # False
print(check_if_last_char_is_a_letter("apple pi e"))  # True
print(check_if_last_char_is_a_letter("apple pi e "))  # False
print(check_if_last_char_is_a_letter(""))  # False



# Another solution:
def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    if txt[-1].isalpha():
        if not txt[-1].islower() and not txt[-1].isupper():
            return True
    return False

# tests
print(check_if_last_char_is_a_letter("apple pie"))  # False
print(check_if_last_char_is_a_letter("apple pi e"))  # True
print(check_if_last_char_is_a_letter("apple pi e "))  # False
print(check_if_last_char_is_a_letter(""))  # False



# Yet another solution:
def check_if_last_char