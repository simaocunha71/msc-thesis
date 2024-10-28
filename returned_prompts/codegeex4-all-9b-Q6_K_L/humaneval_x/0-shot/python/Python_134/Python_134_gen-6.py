def check_if_last_char_is_a_letter(txt):
    import re
    if not txt:
        return False
    if re.search(r'\b\w\W*$', txt):
        return False
    return bool(re.search(r'\w$', txt))

print(check_if_last_char_is_a_letter("apple pie"))
print(check_if_last_char_is_a_letter("apple pi e"))
print(check_if_last_char_is_a_letter("apple pi e "))
print(check_if_last_char_is_a_letter(""))