    if not dict:
        return False
    all_lower = all(isinstance(key, str) and key.islower() for key in dict)
    all_upper = all(isinstance(key, str) and key.isupper() for key in dict)
    return all_lower or all_upper
   # elif all_lower and all_upper:
   #     return True
   # else:
   #     return False
   # for key in dict:
   #     if isinstance(key, str):
   #         if not key.islower() and not key.isupper():
   #             return False
   #     else:
   #         return False
   # return True
   # for key in dict:
   #     if isinstance(key, str):
   #         if key.islower():
   #             return True
   #         elif key.isupper():
   #             return True
   #     else:
   #         return False
   # return False
    #return all(isinstance(key, str) and key.islower() or key.isupper() for key in dict) if dict else False

# Test cases
print(check_dict_case({"a":"apple", "b":"banana"}))  # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))  # True
print(check_dict_case({}))  # False
print(check_dict_case({"a":"apple", "B":"banana", "1":"hello"}))  # False
print(check_dict_case({"A":"apple", "B":"banana", "C":"hello"}))  # False
print(check_dict_case({"a":"apple", "b":"banana", "c":"hello"}))  # True
print(check_dict_case({"STATE":"NC", "ZIP":"12345", "AGE":"36"}))  # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345", "age":"36"}))  # False
print(check_dict_case({"STATE":"NC", "zip":"12345", "age":"36"}))  # True
print(check_dict_case({"STATE":"NC", "ZIP":"12345", "