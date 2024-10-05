    if not txt:
        return False
    
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
    
    if len(txt) == 1:
        return True
    
    prev_char = txt[-2]
    return not prev_char.isalpha()

