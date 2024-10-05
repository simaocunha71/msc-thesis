
def check_dict_case(dict):
    if not dict:
        return False
    if not all(isinstance(key, str) for key in dict.keys()):
        return False
    if not all(isinstance(value, str) for value in dict.values()):
        return False
    if not all(key.islower() for key in dict.keys()):
        return False
    if not all(key.isupper() for key in dict.keys()):
        return False
    return True
