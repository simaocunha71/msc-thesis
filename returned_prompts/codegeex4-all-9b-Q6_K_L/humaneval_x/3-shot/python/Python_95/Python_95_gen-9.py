    if len(dict) == 0:
        return False

    case = None

    for key in dict:
        if not isinstance(key, str):
            return False

        if case is None:
            case = key.islower()
        elif case != key.islower():
            return False

    return True

