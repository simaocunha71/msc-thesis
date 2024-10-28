def check_if_last_char_is_a_letter(txt):
    if txt == "": return False
    return txt[-1].isalpha() and not txt[-1].isalnum()

print(check_if_last_char_is_a_letter("apple pie")) #➞ False
print(check_if_last_char_is_a_letter("apple pi e")) #➞ True
print(check_if_last_char_is_a_letter("apple pi e ")) #➞ False
print(check_if_last_char_is_a_letter("")) #➞ False