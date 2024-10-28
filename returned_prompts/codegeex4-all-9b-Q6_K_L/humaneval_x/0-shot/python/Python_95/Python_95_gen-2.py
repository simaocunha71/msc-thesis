def check_dict_case(dict):
    if len(dict.keys()) == 0:
        return False
    if all(isinstance(key, str) for key in dict.keys()) == False:
        return False
    if all(key.isupper() for key in dict.keys()) or all(key.islower() for key in dict.keys()):
        return True
    else:
        return False

print(check_dict_case({"a":"apple", "b":"banana"}))
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))