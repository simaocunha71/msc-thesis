    def check_if_last_char_is_a_letter(txt):
        last_char = txt[-1]
        if not last_char.isalpha():
            return False
        if not txt.endswith(last_char):
            return True
        return False


