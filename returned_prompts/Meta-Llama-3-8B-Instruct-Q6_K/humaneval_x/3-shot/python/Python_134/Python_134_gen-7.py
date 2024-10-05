    def check_if_last_char_is_a_letter(txt):
        if len(txt) == 0:
            return False
        if txt[-1].isalpha():
            if txt.rstrip().endswith(txt[-1]):
                return False
            return True
        return False


