```
def count_integer(lst):
    return len([x for x in lst if type(x) == int])
```


Explanation:
The function `count_integer` takes a list as input and returns the number of integer elements in the list. It uses a list comprehension to create a new list containing only the integer elements from the input list. The `type(x) == int` condition is used to filter out non-integer elements. The `len` function is then used to count the number of elements in the new list, which represents the number of integer elements in the original list. The unit test `assert count_integer([1,2,'abc',1.2]) == 2` ensures that the function works correctly. 

For example, if the input list is `[1,2,'abc',1.2]`, the function will return `2` because there are two integer elements in the list. If the input list is `[1.2, 'abc', 3.4, 'def']`, the function will return `0` because there are no integer elements in the list. 

This function works with Python 3.x and later versions. In Python 2.x, you would need to use `isinstance(x, (int, long))` instead of `type(x) == int` to correctly identify integer elements. 