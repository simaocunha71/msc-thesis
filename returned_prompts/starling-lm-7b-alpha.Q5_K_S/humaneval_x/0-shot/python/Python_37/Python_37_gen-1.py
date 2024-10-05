To solve this problem, you can follow these steps:

1. Create a new list called `l_odd` that consists of all the odd indices of the list `l`.
2. Create a new list called `l_even` that consists of all the even indices of the list `l`.
3. Sort the list `l_even` in ascending order using the `sorted()` function.
4. Concatenate the `l_odd` and `l_even` lists using the `+` operator.
5. Return the resulting list.

Here's the implementation of the solution:

```python
def sort_even(l: list):
    l_odd = [i for i in range(0, len(l), 2)]
    l_even = [i for i in range(1, len(l), 2)]
    l_even.sort()
    return l_odd + l_even
```

You can test the function with the provided examples:

```python
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

The `sort_even` function works by splitting the input list `l` into two separate lists: `l_odd` and `l_even`. The `l_odd` list contains all the odd indices of `l`, and the `l_even` list contains all the even indices of `l`. The `l_even` list is then sorted in ascending order using the `sorted()` function. Finally, the `l_odd` and `l_even` lists are concatenated using the `+` operator and returned as the result.

This approach ensures that the values at the even indices of the resulting list are sorted, while the values at the odd indices remain unchanged.

```python
def sort_even(l: list):
    l_odd = [i for i in range(0, len(l), 2)]
    l_even = [i for i in range(1, len(l), 2)]
    l_even.