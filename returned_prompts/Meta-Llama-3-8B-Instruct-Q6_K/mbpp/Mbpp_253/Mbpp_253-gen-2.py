```
def count_integer(lst):
    return sum(1 for x in lst if isinstance(x, int))
```


Explanation:
The problem is asking you to write a function that counts the number of integer elements in a given list. The function should return this count.

The unit test provided, `assert count_integer([1,2,'abc',1.2]) == 2`, helps to clarify the problem by showing that the function should return 2 when the input list is `[1,2,'abc',1.2]`. This is because there are two integer elements (1 and 2) in the list.

Here is a Python function that solves the problem:
```
def count_integer(lst):
    return sum(1 for x in lst if isinstance(x, int))
```
This function uses a generator expression to iterate over the list and count the number of elements that are instances of the `int` type. The `sum` function is used to add up these counts, effectively returning the total count of integer elements in the list.