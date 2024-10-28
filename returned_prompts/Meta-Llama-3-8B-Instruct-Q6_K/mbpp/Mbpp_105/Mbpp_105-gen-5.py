```
def count(lst):
    return lst.count(True)
``` 
Explanation:
The problem is asking to create a function that counts the number of True values in a given list. 

The unit test `assert count([True,False,True]) == 2` suggests that the function should return the count of True values in the list. 

The solution uses the built-in `count` method of Python lists, which returns the number of occurrences of the given element (in this case, `True`) in the list. 

So, the function `count` takes a list `lst` as input and returns the count of `True` values in the list. 

For example, if you call `count([True,False,True])`, it will return `2` because there are two `True` values in the list. 