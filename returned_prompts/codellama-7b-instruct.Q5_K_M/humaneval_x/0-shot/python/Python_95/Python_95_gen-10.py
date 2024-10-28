
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    lower_case = True
    upper_case = True
    for key in dict:
        if not isinstance(key, str):
            return False
        if not key.islower():
            lower_case = False
        if not key.isupper():
            upper_case = False
    return lower_case or upper_case