def check_dict_case(dict):
    if len(dict) == 0:
        return False
    if len(dict) == 1:
        if dict.keys()[0].isupper() or dict.keys()[0].islower():
            return True
        else:
            return False
    else:
        for k in dict.keys():
            if k.isupper() != k.islower():
                return False
        return True

B:
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    if len(dict) == 1:
        if dict.keys()[0].isupper() or dict.keys()[0].islower():
            return True
        else:
            return False
    else:
        for k in dict.keys():
            if k.isupper() or k.islower():
                return True
        return False

C:
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    elif len(dict) == 1:
        if dict.keys()[0].isupper() or dict.keys()[0].islower():
            return True
        else:
            return False
    else:
        for k in dict.keys():
            if k.isupper() or k.islower():
                return True
        return False

D:
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    elif len(dict) == 1:
        if dict.keys()[0].isupper() or dict.keys()[0].islower():
            return True
        else:
            return False
    else:
        for k in dict.keys():
            if k.isupper() != k.islower():
                return False
        return True

E:
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    elif len(dict) == 1:
        if dict.keys()[0].isupper() or dict.keys()[0].islower():
            return True
        else:
            return False
    else:
        for k in dict.keys():
            if k.isupper() == k.islower():
                return False
        return True

F:
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    elif len(dict) == 1:
        if dict.keys()[0].isupper() or dict.keys()[0].islower():
            return True
        else:
            return False
    else:
        for k in dict.keys