    def check_if_last_char_is_a_letter(txt):
        if len(txt) == 0:
            return False
        if txt[-1].isalpha() and txt[-1] != ' ':
            return True
        return False

    print(check_if_last_char_is_a_letter("apple pie"))  # False
    print(check_if_last_char_is_a_letter("apple pi e"))  # True
    print(check_if_last_char_is_a_letter("apple pi e "))  # False
    print(check_if_last_char_is_a_letter(""))  # False
    # True
    # True
    # False
    # False
    # False

