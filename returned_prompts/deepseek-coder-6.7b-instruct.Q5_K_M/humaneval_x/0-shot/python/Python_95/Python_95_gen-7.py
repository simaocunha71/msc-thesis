
def check_dict_case(dict):
    if not dict:
        return False
    keys_lower = [key for key in dict.keys() if isinstance(key, str) and key.islower()]
    keys_upper = [key for key in dict.keys() if isinstance(key, str) and key.isupper()]
    return len(keys_lower) == 0 or len(keys_upper) == 0

print(check_dict_case({"a":"apple", "b":"banana"})) # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"})) # True
<jupyter_output>
True
False
False
False
True
<jupyter_text>
