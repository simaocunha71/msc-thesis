
    def check_dict_case(dict):
        if len(dict) == 0:
            return False
        lower = 0
        upper = 0
        for key in dict.keys():
            if key.islower():
                lower += 1
            elif key.isupper():
                upper += 1
            else:
                return False
        if lower == len(dict) or upper == len(dict):
            return True
        else:
            return False

# Test Cases
print(check_dict_case({"a":"apple", "b":"banana"})) # should return True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # should return False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # should return False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # should return False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"})) # should return True

The function works by first checking if the dictionary is empty. If it is, the function returns False. Then it initializes two counters, one for lower case keys and one for upper case keys. It iterates over each key in the dictionary. If the key is lower case, it increments the lower case counter. If the key is upper case, it increments the upper case counter. If the key is neither, it returns False. Finally, it checks if either the lower case counter equals the length of the dictionary or the upper case counter equals the length of the dictionary. If so, it returns True; otherwise, it returns False.
<jupyter_output>
<empty_output>
<jupyter_text>
