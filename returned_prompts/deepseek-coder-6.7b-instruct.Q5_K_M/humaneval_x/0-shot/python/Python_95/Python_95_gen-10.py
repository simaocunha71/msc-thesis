
def check_dict_case(dict):
    lower = 0
    upper = 0

    for key in dict:
        if type(key) is str:
            if key.islower():
                lower += 1
            elif key.isupper():
                upper += 1

    return lower == len(dict) or upper == len(dict)

print(check_dict_case({"a":"apple", "b":"banana"})) # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"})) # True

Explanation:

In the function check_dict_case, we iterate through each key-value pair in the input dictionary. If the key is a string, we check if it's in lower case or upper case and increment the respective counter. If the total number of lower case keys equals the total number of keys in the dictionary, or if the total number of upper case keys equals the total number of keys in the dictionary, we return True. Otherwise, we return False.

This solution has a time complexity of O(n), where n is the number of key-value pairs in the dictionary.
"""

# Test Cases
assert check_dict_case({"a":"apple", "b":"banana"}) == True
assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False
assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False
assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False
assert check_dict_case({"STATE":"NC", "ZIP":"12345"}) == True
assert check_dict_case({}) == False

print("All tests passed.")
<