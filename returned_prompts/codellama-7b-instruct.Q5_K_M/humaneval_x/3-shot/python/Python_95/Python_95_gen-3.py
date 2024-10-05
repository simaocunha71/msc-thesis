    if not dict:
        return False

    if len(dict) == 0:
        return False

    keys = list(dict.keys())
    if all(map(lambda x: x.islower(), keys)):
        return True
    elif all(map(lambda x: x.isupper(), keys)):
        return True
    else:
        return False


