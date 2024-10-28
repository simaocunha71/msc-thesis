To solve this problem, you can first check if the dictionary is empty. If it is, you can return False. Then, you can iterate through the keys in the dictionary and check if each key is a string. If it is, you can check if the key is in uppercase or lowercase. If all keys are either all uppercase or all lowercase, you can return True. Otherwise, you can return False.

Here's one way to implement this solution in Python:

```python
def check_dict_case(dict):
    # Check if the dictionary is empty
    if len(dict) == 0:
        return False

    # Iterate through the keys in the dictionary
    for key in dict.keys():
        # Check if the key is a string
        if isinstance(key, str):
            # Check if the key is in uppercase or lowercase
            if key.isupper():
                # If all keys are in uppercase, return True
                if all(isinstance(k, str) and k.isupper() for k in dict.keys()):
                    return True
            elif key.islower():
                # If all keys are in lowercase, return True
                if all(isinstance(k, str) and k.islower() for k in dict.keys()):
                    return True

    # If any key is not in uppercase or lowercase, return False
    return False
```
You can test the function with the provided examples:

```python
print(check_dict_case({"a":"apple", "b":"banana"}))  # Should return True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # Should return False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # Should return False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # Should return False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))  # Should return True
```

This solution has a time complexity of O(n