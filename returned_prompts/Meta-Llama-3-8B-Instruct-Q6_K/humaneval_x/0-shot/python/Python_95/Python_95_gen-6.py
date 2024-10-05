def check_dict_case(dict):
    if not dict:
        return False
    
    if all(isinstance(key, str) for key in dict.keys()):
        return all(key.islower() for key in dict.keys())
    elif all(isinstance(key, str) for key in dict.keys()):
        return all(key.isupper() for key in dict.keys())
    else:
        return False
# Testing the function
print(check_dict_case({"a":"apple", "b":"banana"})) # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" })) # True
print(check_dict_case({})) # False
print(check_dict_case({"a":1, "b":2})) # False
print(check_dict_case({"a":"apple", "b":"banana", "c":3})) # False
print(check_dict_case({"a":"apple", "b":"banana"})) # True
print(check_dict_case({"A":"apple", "B":"banana"})) # True
print(check_dict_case({"STATE":"NC", "STATE1":"NC1"})) # False
print(check_dict_case({"STATE":"NC", "STATE1":"nc1"})) # True
print(check_dict_case({"STATE":"NC", "STATE1":"NC", "STATE2":"nc1"})) # False
print(check_dict_case({"STATE":"NC", "STATE1":"NC", "STATE2":"NC1"})) # True
print(check_dict_case({"STATE":"NC", "STATE1":"nc", "STATE2":"NC1"})) # False
print(check_dict_case({"STATE":"NC", "STATE1":"nc", "STATE2":"nc"})) # True
print(check_dict_case({"STATE":"NC", "STATE1":"NC1", "STATE2":"NC2"})) # False
print(check_dict_case({"STATE":"NC", "STATE1":"NC1", "STATE2":"nc2"})) # False
print(check_dict_case({"STATE":"NC", "STATE1":"NC1", "STATE2":"nc2"})) # False
print(check_dict_case({"STATE":"NC", "STATE1":"NC1", "