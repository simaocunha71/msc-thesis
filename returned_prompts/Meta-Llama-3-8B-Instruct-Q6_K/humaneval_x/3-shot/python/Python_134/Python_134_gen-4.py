    def check_if_last_char_is_a_letter(txt):
        if not txt: return False
        if txt[-1].isalpha():
            return not txt.rstrip().endswith(txt[-1])
        return False

    print(check_if_last_char_is_a_letter("apple pie")) # False
    print(check_if_last_char_is_a_letter("apple pi e")) # True
    print(check_if_last_char_is_a_letter("apple pi e ")) # False
    print(check_if_last_char_is_a_letter("")) # False
    print(check_if_last_char_is_a_letter("hello")) # False
    print(check_if_last_char_is_a_letter("a")) # True


