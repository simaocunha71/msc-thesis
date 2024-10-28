    def check_if_last_char_is_a_letter(txt):
        if not txt:
            return False
        return txt[-1].isalpha() and not txt[-1].islower()

    return check_if_last_char_is_a_letter(txt)


