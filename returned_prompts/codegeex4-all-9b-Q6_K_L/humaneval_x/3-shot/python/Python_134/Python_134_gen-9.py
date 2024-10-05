    if len(txt) == 0:
        return False
    else:
        last_char = txt[-1]
        if last_char.isalpha() and (txt[-2] == ' ' or txt[-2] == '') and txt[-3] == ' ':
            return True
        else:
            return False

