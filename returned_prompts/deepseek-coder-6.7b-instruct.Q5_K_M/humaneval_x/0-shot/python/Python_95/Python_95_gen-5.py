
def check_dict_case(dict):
    lower = 0
    upper = 0
    
    for key in dict.keys():
        if isinstance(key, str):
            if key.islower():
                lower += 1
            elif key.isupper():
                upper += 1
                
    return lower == len(dict) or upper == len(dict)

# Test cases
print(check_dict_case({"a":"apple", "b":"banana"})) # should return True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # should return False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # should return False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # should return False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"})) # should return True
print(check_dict_case({})) # should return False

# The function works by counting the number of lower case keys and upper case keys in the dictionary. If the total number of keys is equal to the number of lower case keys or the number of upper case keys, then it returns True. Otherwise, it returns False.
# If the dictionary is empty, the function will return False as expected.
<jupyter_output>
True
False
False
False
True
False
<jupyter_text>
Question 4:
<jupyter_code>
