
def check_dict_case(dict):
    if not dict:
        return False
    keys = dict.keys()
    if all(map(lambda x: x.islower(), keys)):
        return True
    if all(map(lambda x: x.isupper(), keys)):
        return True
    return False
