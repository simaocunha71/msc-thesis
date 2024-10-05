    def check_dict_case(dict):
        if not dict:
            return False
        first_key_type = type(next(iter(dict)))
        if first_key_type != str:
            return False
        first_key = next(iter(dict))
        if all(k.islower() for k in dict.keys()) or all(k.isupper() for k in dict.keys()):
            return True
        return False

This will work for python 3.7 and above where dictionary keys are ordered. For previous versions of python, the order of the dictionary keys is not preserved and this function may not work as expected.

