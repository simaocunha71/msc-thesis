
def check_if_last_char_is_a_letter(txt):
    if txt[-1].isalpha() and txt.split()[-1][-1].isalpha() == False:
        return True
    else:
        return False
