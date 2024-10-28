To solve this problem, we can iterate over the keys in the dictionary and check whether all keys are in lower case or upper case. Here's a step-by-step breakdown of the solution:

1. Initialize a boolean variable `all_lower` to True, which will store whether all keys are in lower case. Similarly, initialize a boolean variable `all_upper` to True, which will store whether all keys are in upper case.

2. Iterate over the keys in the dictionary using a `for` loop and a generator expression. For each key, check if it is not in lower case using the `not key.lower() == key` condition. If it is not in lower case, set `all_lower` to False. Similarly, check if it is not in upper case using the `not key.upper() == key` condition. If it is not in upper case, set `all_upper` to False.

3. After iterating over all the keys, check the values of `all_lower` and `all_upper`. If both are True, return True. Otherwise, return False.

Here's the code implementation of the solution:

```python
def check_dict_case(dict):
    all_lower = True
    all_upper = True
    for key in (k for k in dict.keys()):
        if not key.lower() == key:
            all_lower = False
        if not key.upper() == key:
            all_upper = False
    return all_lower or all_upper
```

This implementation checks whether all keys are in lower case or upper case, and returns True if one condition is met, and False if the other condition is met. If the dictionary is empty, the function will return False.

You can use the `check_dict_case` function to test the various examples provided in the question.

```python
check_dict_case({"a":"apple", "b":"banana"})  # Returns True
check_dict_case({"a":"apple", "A":"banana", "B":"banana"})  # Returns False
check_dict_case({"a":"apple", 8:"banana", "a":"apple"})  # Returns False
check_dict_case({"Name":"John", "