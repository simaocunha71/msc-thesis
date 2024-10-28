```
def count_integer(lst):
    return len([x for x in lst if isinstance(x, int)])
```
The function `count_integer` takes a list `lst` as an argument and returns the number of integer elements in the list. It uses a list comprehension to create a list of elements that are integers, and then returns the length of this list. The `isinstance` function is used to check if an element is an integer. This function passes the given unit test `assert count_integer([1,2,'abc',1.2]) == 2`. 

For example, if the input list is `[1,2,'abc',1.2]`, the function will return `2` because there are two integer elements in the list. 

Note: The `isinstance` function checks if an object is an instance or subclass of a class. In this case, it checks if an element is an instance of the `int` class, which means it checks if the element is an integer. 

This function works with both positive and negative integers, as well as with zero. It also works with floating point numbers, but they are not considered as integer elements. For example, the function will return `1` for the list `[1,2,'abc',1.2]`, but it will return `1` for the list `[1,2,'abc',1]` as well. 

The function is case sensitive, so it will not consider strings that represent integers as integer elements. For example, the function will return `0` for the list `[1,2,'abc','1']`, because `'1'` is a string, not an integer. 

The function is also able to handle empty lists, in which case it will return `0`. For example, the function will return `0` for the list `[]`. 