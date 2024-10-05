def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    return txt[-1].isalpha() and txt[-1] not in "a e i o u A E I O U"

print(check_if_last_char_is_a_letter("apple pie")) # ➞ False
print(check_if_last_char_is_a_letter("apple pi e")) # ➞ True
print(check_if_last_char_is_a_letter("apple pi e ")) # ➞ False
print(check_if_last_char_is_a_letter("")) # ➞ False