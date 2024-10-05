    keys = dict.keys()
    upper = False
    lower = False
    for key in keys:
        if not key.isupper():
            upper = True
        if not key.islower():
            lower = True
    return upper and lower


