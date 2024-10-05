```
def check_dict_case(dict):
    if not dict:
        return False
    all_lower = all(isinstance(key, str) and key.islower() for key in dict)
    all_upper = all(isinstance(key, str) and key.isupper() for key in dict)
    return all_lower or all_upper
```



The function `check_dict_case` takes a dictionary as an argument. It first checks if the dictionary is empty. If it is, it returns `False`. Then it checks if all keys in the dictionary are strings in lower case or all keys are strings in upper case. It uses the `isinstance` function to check if each key is a string, and the `islower` and `isupper` methods to check if the key is in lower case or upper case. The `all` function is used to check if all keys in the dictionary satisfy the condition. If any key does not satisfy the condition, the function returns `False`. If all keys satisfy the condition, the function returns `True`. 





Example:
```
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))  # returns True
print(check_dict_case({"a":"apple", "b":"banana" }))  # returns True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana" }))  # returns False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple" }))  # returns False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston" }))  # returns False
```



The function `check_dict_case` correctly identifies whether all keys in a dictionary are in lower case or upper case, and returns `True` or `False` accordingly. It also returns `False` if the dictionary is empty. 