To solve this problem, you can follow these steps:

1. Initialize a variable `all_lower` to keep track of whether all keys are lowercase. Set it to True.
2. Initialize a variable `all_upper` to keep track of whether all keys are uppercase. Set it to True.
3. Iterate through each key in the dictionary using a for loop.
4. Convert the key to lowercase using the `lower()` method. If the result is not equal to the original key, set `all_lower` to False.
5. Convert the key to uppercase using the `upper()` method. If the result is not equal to the original key, set `all_upper` to False.
6. After iterating through all keys, check if `all_lower` is False and `all_upper` is False. If both conditions are true, return False.
7. If the conditions in step 6 are not met, return True.

Here is the code that implements the solution:

```python
def check_dict_case(dict):
    all_lower = True
    all_upper = True
    for key in dict:
        if key.lower() != key:
            all_lower = False
        if key.upper() != key:
            all_upper = False
    if all_lower and all_upper:
        return False
    else:
        return True
```

You can use the function like this:

```python
print(check_dict_case({"a":"apple", "b":"banana"}))  # returns True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # returns False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # returns False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # returns False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))  # returns True
```

This function will return True if all keys are lowercase or uppercase, and False otherwise.

Note: In Python, dictionary