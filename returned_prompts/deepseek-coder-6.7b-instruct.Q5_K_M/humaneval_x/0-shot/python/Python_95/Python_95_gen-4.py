
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
    return lower == len(dict) or upper == len(dict)

print(check_dict_case({"a":"apple", "b":"banana"})) # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"})) # True
print(check_dict_case({})) # False

#This solution works by iterating through the dictionary keys. 
#If a key is lowercase, it increments the lower variable by one. 
#If a key is uppercase, it increments the upper variable by one. 
#If a key is neither, the function returns False. 
#Finally, the function returns True if all keys are either lower or upper case.
<jupyter_output>
True
False
False
False
True
False
<jupyter_text>
Problem 7: Write a Python function that takes a list of strings and returns a new list with all strings that start with a vowel.
<jupyter_code>
