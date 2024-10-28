```
def check_tuplex(tuplex, element):
    return element in tuplex
```
This function takes a tuple `tuplex` and an element `element` as input, and returns `True` if the element exists in the tuple, and `False` otherwise. The `in` operator is used to check if the element is present in the tuple. The unit test `assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True` ensures that the function works correctly.