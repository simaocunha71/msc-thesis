
def check_dict_case(dict):
    if not dict:
        return False
    lower_keys = [k for k in dict.keys() if isinstance(k, str) and k.islower()]
    upper_keys = [k for k in dict.keys() if isinstance(k, str) and k.isupper()]
    return len(lower_keys) == len(dict) or len(upper_keys) == len(dict)

print(check_dict_case({"a":"apple", "b":"banana"}))  # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))  # True
print(check_dict_case({}))  # False

This program works by first checking if the given dictionary is empty. If it is, the function returns False. If not, it creates two lists - one for keys that are all in lower case, and one for keys that are all in upper case. It then checks if the length of these lists is equal to the length of the dictionary. If it is, that means all keys are either all in lower case or all in upper case, so the function returns True. Otherwise, it returns False.

This function works by iterating over all keys in the dictionary, checking if they are strings, and then checking if they are all in lower case or all in upper case. It uses list comprehension to create these lists in a single line of code. It then checks if the length of these lists is equal to the length of the dictionary.

It's important to note that this function assumes that all keys in the dictionary are either strings or integers. If there are non-string or non-integer keys in the dictionary, the function may not behave as expected.
    """
<jupyter_output>
<empty_output>
<jupyter_text>
