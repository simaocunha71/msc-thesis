def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    last_char = txt[-1]
    if last_char.isalpha() and not last_char.isalnum():
        return True
    return False

print(check_if_last_char_is_a_letter("apple pie")) # ➞ False
print(check_if_last_char_is_a_letter("apple pi e")) # ➞ True
print(check_if_last_char_is_a_letter("apple pi e ")) # ➞ False
print(check_if_last_char_is_a_letter("")) # ➞ False