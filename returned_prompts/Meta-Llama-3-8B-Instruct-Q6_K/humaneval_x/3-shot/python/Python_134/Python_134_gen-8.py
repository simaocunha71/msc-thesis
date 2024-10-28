    def check_if_last_char_is_a_letter(txt):
        if not txt:  # if string is empty
            return False
        words = txt.split()  # split the string into words
        last_char = txt[-1]  # get the last character
        if len(words) > 0 and txt[-1] in words[-1]:  # check if last character is part of last word
            return False
        return last_char.isalpha()  # check if last character is alphabetical


