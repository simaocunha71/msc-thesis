```
def check_tuplex(tuplex, target):
    return target in tuplex
```


This function checks whether the target element exists within the tuple. The `in` operator is used to check for membership in the tuple. If the target element is found, the function returns `True`; otherwise, it returns `False`. The function also includes a unit test to verify its correctness. The unit test checks whether the target element 'r' exists in the tuple and expects the function to return `True`. 

Here is the unit test:
```
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
``` 