    if txt == "":
        return False

    last_char = txt[-1]

    if last_char.isalpha():
        if txt.find(" ", len(txt) - 1, len(txt)) == len(txt) - 1:
            return True
        else:
            return False
    else:
        return False


