```
def new_tuple(lst, str):
    return tuple(lst + [str])
```


In this problem, we need to create a new tuple from a given string and list. The string will be added to the end of the list, and then the list will be converted to a tuple. This is confirmed by the unit test `assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')`. 

We can achieve this by using the `+` operator to concatenate the list and the list containing the string, and then converting the result to a tuple using the `tuple()` function. The `+` operator is used to concatenate lists in Python, and it returns a new list that contains all the elements from both lists. 

Here is the solution:
```
def new_tuple(lst, str):
    return tuple(lst + [str])
```


This function takes two arguments, `lst` and `str`, where `lst` is a list and `str` is a string. It concatenates `lst` with a new list containing `str`, and then converts the result to a tuple using the `tuple()` function. The resulting tuple is then returned by the function. 

For example, if we call `new_tuple(["WEB", "is"], "best")`, the function will return the tuple `('WEB', 'is', 'best')`. This is confirmed by the unit test provided. 

This solution is efficient and easy to understand, and it meets the requirements of the problem. 