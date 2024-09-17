```
def check_tuplex(t, e):
    return e in t
```
This function takes two parameters, `t` which is a tuple and `e` which is the element to be checked. It returns `True` if the element exists in the tuple and `False` otherwise. 

The unit test provided, `assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True`, suggests that the function should return `True` when the element 'r' is found in the tuple. This function will pass this test. 