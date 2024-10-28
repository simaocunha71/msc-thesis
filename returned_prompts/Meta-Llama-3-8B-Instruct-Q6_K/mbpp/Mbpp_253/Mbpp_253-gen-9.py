```
def count_integer(lst):
    return len([x for x in lst if isinstance(x, int)])
```



The problem is asking to create a Python function that takes a list as an input and returns the number of integer elements in that list. 

The unit test provided, `assert count_integer([1,2,'abc',1.2]) == 2`, suggests that the function should count the number of integers in the list, regardless of whether they are positive, negative or zero.

The provided solution uses a list comprehension to create a new list that includes only the integer elements from the input list. The `isinstance` function is used to check if an element is an integer. The `len` function is then used to count the number of elements in the new list, which is the number of integer elements in the original list.

Here's how you can use this function:

```
print(count_integer([1,2,'abc',1.2]))  # Output: 2
```



This function will return `2` because there are two integer elements in the list: `1` and `2`. The other elements in the list are not integers: `'abc'` is a string and `1.2` is a float.