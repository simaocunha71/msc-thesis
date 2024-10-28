
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    elif all(isinstance(i, str) and i.isupper() for i in dict.keys()):
        return True
    elif all(isinstance(i, str) and i.islower() for i in dict.keys()):
        return True
    else:
        return False




# Test cases
print(check_dict_case({"a":"apple", "b":"banana"}))  # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))  # True

# More test cases
print(check_dict_case({}))  # False
print(check_dict_case({"key":"value"}))  # False
print(check_dict_case({1:"value"}))  # False
print(check_dict_case({"Key":"Value"}))  # True
print(check_dict_case({"KEY":"VALUE"}))  # True
print(check_dict_case({"Key1":"Value1", "Key2":"Value2"}))  # False
print(check_dict_case({"Key1":"Value1", "Key2":"Value2", "Key3":"Value3"}))  # True




















































































































