To solve this problem, you can define a function called `check_dict_case` that takes a dictionary as input. Inside the function, you can initialize two variables `lower_case` and `upper_case` to keep track of the lowercase and uppercase keys. Then, you can iterate through the dictionary using a for loop and check if each key is a string in lowercase or uppercase using the `isupper()` and `islower()` methods. If the key is in lowercase, you can increment the `lower_case` variable, and if the key is in uppercase, you can increment the `upper_case` variable. After iterating through all the keys, you can check if both `lower_case` and `upper_case` are equal to the length of the dictionary. If they are, you can return True, otherwise, you can return False.

Here's the code for the solution:

```python
def check_dict_case(dict):
    lower_case = 0
    upper_case = 0
    for key in dict:
        if isinstance(key, str) and key.islower():
            lower_case += 1
        elif isinstance(key, str) and key.isupper():
            upper_case += 1
    if lower_case == len(dict) or upper_case == len(dict):
        return True
    else:
        return False
```

You can test the function using the provided examples:

```python
print(check_dict_case({"a":"apple", "b":"banana"}))  # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))  # True
```

The function will return True if all keys are strings in lowercase or uppercase, and False otherwise.

I hope this helps! Let me