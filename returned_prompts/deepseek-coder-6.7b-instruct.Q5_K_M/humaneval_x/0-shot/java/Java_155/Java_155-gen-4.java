
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    lower_case = [k.islower() for k in dict.keys()]
    upper_case = [k.isupper() for k in dict.keys()]
    return all(lower_case) or all(upper_case)

# Test cases
print(check_dict_case({"a":"apple", "b":"banana"})) # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" })) # True
<jupyter_output>
True
False
False
False
True
<jupyter_text>
Question 2
<jupyter_code>
