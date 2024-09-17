The problem is asking to create a function that counts the number of integer elements in a given list. 

The unit test `assert count_integer([1,2,'abc',1.2]) == 2` suggests that the function should count both positive and negative integers. 

Here's a Python function that solves the problem:
```
def count_integer(lst):
    return sum(isinstance(x, int) for x in lst)
```
This function uses a generator expression to iterate over the list and check if each element is an instance of the `int` class using the `isinstance` function. The `sum` function then counts the number of `True` values (i.e., the number of integers in the list). 

For example, if you call `count_integer([1,2,'abc',1.2])`, the function will return `2`, which is the number of integer elements in the list. 

Note that this function considers `1.2` as a float and not an integer, so it won't be counted. If you want to count floats as integers, you can modify the function to use `isinstance(x, (int, float))`. However, this would also count `1.2` as an integer, so the function's behavior would change.  You can choose the behavior that best fits your needs. 