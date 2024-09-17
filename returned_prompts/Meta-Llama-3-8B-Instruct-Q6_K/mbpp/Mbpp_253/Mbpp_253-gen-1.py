You can solve this problem by using a list comprehension to filter out non-integer elements from the list, and then get the length of the resulting list.

Here is the Python function that does this:

```python
def count_integer(lst):
    return len([x for x in lst if isinstance(x, int)])
```

This function works by iterating over each element `x` in the input list `lst`. It checks if `x` is an instance of the `int` type using the `isinstance` function. If `x` is an `int`, it includes it in the list comprehension. The list comprehension creates a new list containing only the integer elements from the original list. The `len` function is then used to get the length of this new list, which is the number of integer elements in the original list. 

For example, if you call `count_integer([1,2,'abc',1.2])`, the function will return `2` because there are two integer elements in the list. 

The unit test `assert count_integer([1,2,'abc',1.2]) == 2` ensures that the function works correctly. It checks that the function returns `2` when given the list `[1,2,'abc',1.2]`. If the function is correct, this test will pass; otherwise, it will fail. 

This function will work correctly for any list containing integer and non-integer elements. It is flexible and can handle lists of any size. 

Note: This function does not count floating point numbers as integers. If you want to count floating point numbers as integers, you can modify the function to use `isinstance(x, (int, float))` instead of `isinstance(x, int)`. This will include both integer and floating point numbers in the count. 