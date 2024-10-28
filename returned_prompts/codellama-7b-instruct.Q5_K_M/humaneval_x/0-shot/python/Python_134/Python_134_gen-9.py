
def check_if_last_char_is_a_letter(txt):
    if txt[-1] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if " " in txt[-2:]:
            return False
        else:
            return True
    else:
        return False