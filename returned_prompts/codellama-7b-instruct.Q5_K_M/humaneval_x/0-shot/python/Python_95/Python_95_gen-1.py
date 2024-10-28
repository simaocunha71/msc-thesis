
def check_dict_case(dict):
    if not dict:
        return False
    if all(isinstance(k, str) and k.isupper() for k in dict.keys()):
        return all(isinstance(v, str) and v.isupper() for v in dict.values())
    return all(isinstance(v, str) and v.islower() for v in dict.values())
