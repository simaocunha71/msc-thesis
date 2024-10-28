```
def check_tuplex(tuplex, element):
    return element in tuplex
```
The function `check_tuplex` takes in a tuple `tuplex` and an element `element` as arguments. It then checks if the element exists within the tuple using the `in` operator. The function returns `True` if the element is found in the tuple, and `False` otherwise. 

For example, if we call `check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r')`, the function will return `True` because 'r' is indeed an element in the tuple.  This is confirmed by the unit test `assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True`. 

The `in` operator is used to check if an element exists in a sequence (like a tuple or list). It returns `True` if the element is found in the sequence and `False` otherwise. This operator is a common and efficient way to check if an element is present in a sequence. 