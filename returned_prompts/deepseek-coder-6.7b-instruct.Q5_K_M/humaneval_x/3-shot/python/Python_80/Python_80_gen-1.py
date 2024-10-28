    for i in range(len(s)-2):
        if len(set(s[i:i+3])) != 3:
            return False
    return True


