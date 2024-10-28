    if not txt:  # if the string is empty
        return False

    if txt[-1].isalpha() and not txt[-1].isalnum():  # if last char is a letter and not part of word
        return True

    return False
