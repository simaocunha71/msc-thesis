    if a**2 + b**2 == c**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    elif b**2 + c**2 == a**2:
        return True
    else:
        return False

