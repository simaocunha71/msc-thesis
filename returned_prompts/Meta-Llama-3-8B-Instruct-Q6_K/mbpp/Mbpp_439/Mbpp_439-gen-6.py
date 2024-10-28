```
def multiple_to_single(lst):
    return int(''.join(str(x) for x in lst))
```


This function works by first converting each integer in the list to a string, then joining all the strings together into one, and finally converting the resulting string back to an integer. The unit test `assert multiple_to_single([11, 33, 50])==113350` demonstrates the expected behavior of this function.