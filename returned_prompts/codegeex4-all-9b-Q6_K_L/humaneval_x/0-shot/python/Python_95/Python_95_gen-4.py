def check_dict_case(dict):
    if not dict: return False
    for key in dict.keys():
        if type(key) != str:
            return False
        if key.isupper() == False and key.islower() == False:
            return False
    return True
print(check_dict_case({"a":"apple", "b":"banana"}))
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))

print(check_dict_case({}))

print(check_dict_case({"a":"apple", "b":"banana"}))

print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))

print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))

print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))

print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))

print(check_dict_case({}))