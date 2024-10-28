The problem is asking to find the cumulative sum of all the values in a list of tuples. 

However, the problem doesn't specify the order in which the values should be added. But, based on the unit test provided, `assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30`, it seems that the values should be flattened and then summed.

Here is the Python function that solves the problem:

```python
def cummulative_sum(tuples_list):
    return sum(sum(i) for i in tuples_list)
```

This function uses a generator expression to flatten the list of tuples, and then the built-in `sum` function to calculate the cumulative sum. 

For example, if we call `cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])`, it will return `30`, which is the sum of `1+3+5+6+7+2+6`. 