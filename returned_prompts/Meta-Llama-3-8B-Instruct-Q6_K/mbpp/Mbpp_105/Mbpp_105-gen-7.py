```
def count(lst):
    return sum(1 for item in lst if item)
```



Explanation:
This problem is asking you to write a function that takes a list of boolean values as input and returns the count of True values in the list.

The given unit test `assert count([True,False,True]) == 2` suggests that the function should return 2 for the input `[True, False, True]` because there are two True values in the list.

We can solve this problem by using a generator expression inside the `sum` function. The generator expression iterates over the list and returns 1 for each True value and 0 for each False value. The `sum` function then adds up these values to give the total count of True values.

Here's the Python code for the solution:

```
def count(lst):
    return sum(1 for item in lst if item)
```

This function works by iterating over each item in the list. For each item, it checks if the item is True. If the item is True, it adds 1 to the sum. If the item is False, it adds 0 to the sum. The sum of all these 1s and 0s is the total count of True values in the list. This count is then returned by the function.