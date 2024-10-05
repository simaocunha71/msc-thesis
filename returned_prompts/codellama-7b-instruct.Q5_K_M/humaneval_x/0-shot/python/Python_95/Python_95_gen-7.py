
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    if len(dict) == 1:
        return True
    lower_case = True
    upper_case = True
    for key in dict:
        if not key.islower():
            lower_case = False
        if not key.isupper():
            upper_case = False
    if lower_case or upper_case:
        return True
    else:
        return False
