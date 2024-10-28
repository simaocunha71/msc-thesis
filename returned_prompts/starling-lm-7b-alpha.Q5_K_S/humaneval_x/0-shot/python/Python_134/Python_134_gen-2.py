
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    if txt[-1].isalpha():
        if txt[-1] != ' ':
            return True
    return False


# Alternative solution
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    return txt[-1].isalpha() and txt.rfind(" ") != txt.rfind(txt[-1])




# Another alternative solution
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    return txt[-1].isalpha() and txt.rstrip().endswith(txt[-1])



# Another alternative solution
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    return txt[-1].isalpha() and txt.count(txt[-1]) == 1


# Pythonic way
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    return (txt[-1].isalpha() and
            txt.rpartition(" ")[-1] == txt[-1])






# Pythonic way
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    return (txt[-1].isalpha() and
            txt.rpartition(" ")[-1] == txt[-1])















































































































