    def check_if_last_char_is_a_letter(txt):
        if len(txt) == 0:
            return False
        words = txt.split()
        if len(words) == 0:
            return False
        last_word = words[-1]
        last_char = last_word[-1]
        if last_char.isalpha():
            return last_word[-1] == ' '
        else:
            return False

    print(check_if_last_char_is_a_letter("apple pie"))  # False
    print(check_if_last_char_is_a_letter("apple pi e"))  # True
    print(check_if_last_char_is_a_letter("apple pi e "))  # False
    print(check_if_last_char_is_a_letter(""))  # False
    print(check_if_last_char_is_a_letter("a"))  # True
    print(check_if_last_char_is_a_letter("1"))  # False


