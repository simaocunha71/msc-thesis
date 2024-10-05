def check_if_last_char_is_a_letter(txt):
    return bool(txt.strip() and txt[-1].isalpha() and txt[-2] != " ") if txt else False

print(check_if_last_char_is_a_letter("apple pie")) # ➞ False
print(check_if_last_char_is_a_letter("apple pi e")) # ➞ True
print(check_if_last_char_is_a_letter("apple pi e ")) # ➞ False
print(check_if_last_char_is_a_letter("")) # ➞ False