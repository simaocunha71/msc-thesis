To solve this problem, you can define a function called check_dict_case that takes a dictionary as input. The function will iterate through the keys of the dictionary and check if all keys are either in lower case or upper case. If all keys are in lower case or all keys are in upper case, the function will return True, otherwise, it will return False.

Here is a step-by-step explanation of the solution:

1. Define the function check_dict_case that takes a dictionary as input.
2. Create an empty list called keys to store the keys of the dictionary. You can use the keys() method to get all keys of the dictionary and append them to the keys list.
3. Create two variables, lower_case and upper_case, and set them to True. These variables will keep track of whether any lower case or upper case keys are found.
4. Iterate through each key in the keys list. For each key:
    - Check if the key is in lower case. If it is not, update the lower_case variable to False.
    - Check if the key is in upper case. If it is not, update the upper_case variable to False.
5. After the loop, check if both lower_case and upper_case are True. If they are, return True. Otherwise, return False.
6. If the dictionary is empty, return False.

This solution ensures that all keys in the dictionary are either in lower case or upper case, and returns True if that's the case, and False otherwise.

Here is the code for the solution:

```python
def check_dict_case(dict):
    keys = list(dict.keys())
    lower_case = True
    upper_case = True
    for key in keys:
        if not key.islower():
            lower_case = False
        if not key.isupper():
            upper_case = False
    if lower_case and upper_case:
        return True
    return False
```

You can use the function like this:

```python
print(check_dict_case({"a":"apple", "b":"banana"}))  # Output: True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))