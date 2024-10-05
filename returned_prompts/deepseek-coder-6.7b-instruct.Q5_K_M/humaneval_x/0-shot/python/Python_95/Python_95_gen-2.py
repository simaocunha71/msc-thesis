
def check_dict_case(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    if all(key.islower() for key in keys) or all(key.isupper() for key in keys):
        return True
    return False

# Test cases
print(check_dict_case({"a":"apple", "b":"banana"})) # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"})) # True
print(check_dict_case({})) # False
<jupyter_output>
True
False
False
False
True
False
<jupyter_text>
