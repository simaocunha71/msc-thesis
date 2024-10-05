    def check_if_last_char_is_a_letter(txt):
        if not txt:
            return False
        if txt[-1].isalpha():
            return True
        if ' ' in txt:
            return False
        return True


