    keys = dict.keys()
    if len(keys) == 0:
        return False
    if set(keys[0][0] for keys in dict.keys()) == {'lower'} or set(keys[0][0] for keys in dict.keys()) == {'upper'}:
        return True
    else:
        return False



