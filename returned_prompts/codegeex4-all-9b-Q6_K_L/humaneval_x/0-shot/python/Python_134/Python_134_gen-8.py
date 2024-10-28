def check_if_last_char_is_a_letter(txt):
    return txt and txt[-1].isalpha() and txt[-1] not in " ".join(txt.split())

print(check_if_last_char_is_a_letter("apple pie")) #➞ False
print(check_if_last_char_is_a_letter("apple pi e")) #➞ True
print(check_if_last_char_is_a_letter("apple pi e ")) #➞ False
print(check_if_last_char_is_a_letter("")) #➞ False