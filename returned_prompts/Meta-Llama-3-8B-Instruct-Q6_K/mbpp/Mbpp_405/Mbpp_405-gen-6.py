```
def check_tuplex(tuplex, element):
    return element in tuplex
```


This function takes a tuple and an element as input and returns True if the element is present in the tuple, False otherwise. The unit test provided ensures that the function works correctly for the given tuple and element. For example, the test `assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True` checks that the function returns True when the element 'r' is present in the tuple. 

The function uses the in keyword to check if the element is present in the tuple. The in keyword returns True if the element is found in the tuple, and False otherwise. 

The function can be used like this:
```
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(check_tuplex(tuplex, 'r'))  # Returns: True
print(check_tuplex(tuplex, 'x'))  # Returns: False
``` 