```
def find_tuples(tuples, k):
    result = []
    for tup in tuples:
        if all(i % k == 0 for i in tup):
            result.append(tup)
    return result
```

Explanation:
The function `find_tuples` takes in a list of tuples and an integer `k`. It initializes an empty list `result` to store the tuples that satisfy the condition. 

Next, it iterates over each tuple `tup` in the given list of tuples. For each tuple, it uses a generator expression with the `all` function to check if all the elements in the tuple are divisible by `k`. The `all` function returns `True` if all elements in the generator expression evaluate to `True`, otherwise it returns `False`.

If all the elements in the tuple are divisible by `k`, the tuple is appended to the `result` list. 

Finally, the function returns the `result` list containing the tuples that satisfy the condition.

In the provided example, the function is called with the list `[(6, 24, 12), (7, 9, 6), (12, 18, 21)]` and the integer `6`. The function returns `[(6, 24, 12)]` because only the first tuple has all of its elements divisible by 6.

Note: The `all` function is a built-in Python function that returns `True` if all elements in the iterable (in this case, the generator expression) are `True`. Otherwise, it returns `False`.

To use the function, you can simply call it with your list of tuples and the integer `k`. The function will return a new list containing the tuples that satisfy the condition.

Here's an example usage:
```python
print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))  # Output: [(6, 24, 12)]
```

This will output `[(6, 24, 12)]`, as it is the