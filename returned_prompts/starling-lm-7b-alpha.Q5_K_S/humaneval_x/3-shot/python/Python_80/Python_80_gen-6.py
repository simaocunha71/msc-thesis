    if len(s) < 3:
        return False
    if len(set(s[:3])) == 3:
        return True
    else:
        return is_happy(s[1:])


