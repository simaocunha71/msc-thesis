
def check_dict_case(dict):
    if not dict:
        return False
    lower_case = all(k.islower() for k in dict.keys())
    upper_case = all(k.isupper() for k in dict.keys())
    return lower_case or upper_case

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
Q2:
<jupyter_code>
