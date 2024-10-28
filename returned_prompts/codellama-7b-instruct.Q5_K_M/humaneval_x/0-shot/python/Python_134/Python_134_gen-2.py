
def check_if_last_char_is_a_letter(txt):
    if txt == "":
        return False
    else:
        if txt[-1].isalpha():
            if txt.count(" ") == 0:
                return True
            else:
                return False
        else:
            return False
