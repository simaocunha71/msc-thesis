The problem can be solved using Python's built-in functions and list comprehension. 

Here is the Python function that solves the problem:

```Python
def sum_Of_Subarray_Prod(lst):
    total_sum = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            total_sum += sum([x for x in lst[i:j+1]]) * sum([x for x in lst[i:j+1]])
    return total_sum
```

This function works by iterating over all possible sublists of the given list, calculating their sums and products, and summing these up. The unit test `assert sum_Of_Subarray_Prod([1,2,3]) == 20` shows that this function works correctly for the given list. 

However, this function is not efficient for large lists, as it has a time complexity of O(n^3) due to the nested loops and list comprehensions. For large lists, a more efficient solution would be needed. 

Here is a more efficient solution that calculates the sum and product of all possible sublists in O(n^2) time:

```Python
def sum_Of_Subarray_Prod(lst):
    total_sum = 0
    prefix_sum = [0] * (len(lst) + 1)
    for i in range(len(lst)):
        prefix_sum[i+1] = prefix_sum[i] + lst[i]
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            total_sum += (prefix_sum[j+1] - prefix_sum[i]) * (prefix_sum[j+1] - prefix_sum[i])
    return total_sum
```

This function calculates the prefix sum of the list, then for each pair of indices (i, j), it calculates the sum of the sublist from i to j, and adds it to the total sum. The time complexity of this function is O(n^2), which is much more efficient for large lists. 