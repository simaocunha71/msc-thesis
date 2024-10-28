    if not dict:
        return False

    keys = dict.keys()
    key_list = [key.lower() for key in keys]
    if key_list == keys:
        return True
    else:
        key_list = [key.upper() for key in keys]
        if key_list == keys:
            return True
        else:
            return False


