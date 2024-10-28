
def check_if_last_char_is_a_letter(txt):
    last_char = txt[-1]
    return last_char.isalpha() and not last_char.isalnum()
