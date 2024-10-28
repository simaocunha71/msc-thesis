
def check_dict_case(dict):
    if not dict:
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

print(check_dict_case({"a":"apple", "b":"banana"})) # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"})) # True
print(check_dict_case({})) # False


This code works by iterating over the keys in the dictionary and checking if each key is either entirely lower case or entirely upper case. If a key is not in either case, the function immediately returns False. It then checks if the number of keys that are entirely lower case or entirely upper case is equal to the total number of keys in the dictionary. If it is, the function returns True, otherwise it returns False.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
