def check_dict_case(dict):
    if not dict:
        return False
    else:
        keys = dict.keys()
        lower_case = all(key.islower() for key in keys)
        upper_case = all(key.isupper() for key in keys)
        return lower_case or upper_case

print(check_dict_case({"a":"apple", "b":"banana"})) # should return True.
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # should return False.
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # should return False.
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # should return False.
print(check_dict_case({"STATE":"NC", "ZIP":"12345" })) # should return True.