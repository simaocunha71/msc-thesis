
    if not dict:
        return False

    lower_case = all(key.islower() for key in dict.keys())
    upper_case = all(key.isupper() for key in dict.keys())

    if lower_case or upper_case:
        return True
    else:
        return False

# Test cases:
print(check_dict_case({"a":"apple", "b":"banana"}))  # Expected: True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # Expected: False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # Expected: False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # Expected: False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))  # Expected: True
print(check_dict_case({}))  # Expected: False
<jupyter_output>
True
False
False
False
True
False
<jupyter_text>
Problem 2:
<jupyter_code>
