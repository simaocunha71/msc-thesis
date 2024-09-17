```
def count(lst):
    return sum(map(bool, lst))
```


Explanation:
The given problem asks for a function that counts the number of True boolean values in a given list. 

The function should return the count of True boolean values, not the number of True and False values. 

The unit test `assert count([True,False,True]) == 2` clarifies that the function should count the number of True boolean values, which is 2 in this case.

The function `count` uses the built-in `map` function to apply the `bool` function to each element in the list, effectively converting all elements to boolean values (True or False). The `sum` function is then used to count the number of True boolean values.

For example, if the input list is `[True,False,True]`, the `map` function will convert it to `[True,False,True]`, and the `sum` function will count the number of True values, which is 2. Therefore, the output of the function `count([True,False,True])` is 2. 