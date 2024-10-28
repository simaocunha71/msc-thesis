
def check_if_last_char_is_a_letter(txt):
    if len(txt) > 0:
        if txt[-1].isalpha() and (txt.rfind(" ") == txt.rfind(txt[-1])):
            return True
        else:
            return False
    else:
        return False

check_if_last_char_is_a_letter("apple pie")  # False
check_if_last_char_is_a_letter("apple pi e")  # True
check_if_last_char_is_a_letter("apple pi e ")  # False
check_if_last_char_is_a_letter("")  # False







def check_if_last_char_is_a_letter(txt):
    if len(txt) > 0:
        if txt[-1].isalpha() and (txt.rfind(" ") == txt.rfind(txt[-1])):
            return True
        else:
            return False
    else:
        return False

check_if_last_char_is_a_letter("apple pie")  # False
check_if_last_char_is_a_letter("apple pi e")  # True
check_if_last_char_is_a_letter("apple pi e ")  # False
check_if_last_char_is_a_letter("")  # False







def check_if_last_char_is_a_letter(txt):
    if len(txt) > 0:
        if txt[-1].isalpha() and (txt.rfind(" ") == txt.rfind(txt[-1])):
            return True
        else:
            return False
    else:
        return False

check_if_last_char_is_a_letter("apple pie")  # False
check_if_last_char_is_a_letter("apple pi e")  # True
check_if_last_char_is_a_letter("apple pi e ")  # False
check_if_last_char_is_a_letter("")  # False







def