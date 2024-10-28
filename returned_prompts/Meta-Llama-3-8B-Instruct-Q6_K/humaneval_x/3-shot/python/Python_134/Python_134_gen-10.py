    def check_if_last_char_is_a_letter(txt):
        if len(txt) == 0:
            return False
        if txt[-1].isalpha() and not txt[-1].isalnum():
            return True
        return False

    print(check_if_last_char_is_a_letter("apple pie"))  # False
    print(check_if_last_char_is_a_letter("apple pi e"))  # True
    print(check_if_last_char_is_a_letter("apple pi e "))  # False
    print(check_if_last_char_is_a_letter(""))  # False
    print(check_if_last_char_is_a_letter("a"))  # True
    print(check_if_last_char_is_a_letter("123"))  # False
    print(check_if_last_char_is_a_letter("a1"))  # False
    print(check_if_last_char_is_a_letter("abc"))  # True
    print(check_if_last_char_is_a_letter("123abc"))  # False
    print(check_if_last_char_is_a_letter("abc123"))  # True
    print(check_if_last_char_is_a_letter("a"))  # True
    print(check_if_last_char_is_a_letter("123"))  # False
    print(check_if_last_char_is_a_letter("a1"))  # False
    print(check_if_last_char_is_a_letter("abc"))  # True
    print(check_if_last_char_is_a_letter("123abc"))  # False
    print(check_if_last_char_is_a_letter("abc123"))  # True
    print(check_if_last_char_is_a_letter("a"))  # True
    print(check_if_last_char_is_a_letter("123"))  # False
    print(check_if_last_char_is_a_letter("a1"))  # False
    print(check_if_last_char_is_a_letter("abc"))  # True
    print(check_if_last_char_is_a_letter("123abc"))  # False
    print(check_if_last_char_is_a_letter("abc123"))  # True
    print(check_if_last_char_is_a_letter("a"))  # True
    print(check_if_last_char_is_a_letter("123"))  # False
    print(check_if_last_char_is_a_letter("a1"))  # False
    print(check_if_last_char_is_a_letter("abc"))  # True
    print(check_if_last_char_is_a_letter("123abc"))  # False
    print(check_if_last_char_is_a_letter("abc123"))  # True