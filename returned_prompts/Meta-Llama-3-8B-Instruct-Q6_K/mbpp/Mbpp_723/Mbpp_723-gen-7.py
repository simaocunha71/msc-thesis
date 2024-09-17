```
def count_same_pair(list1, list2):
    return sum(x == y for x, y in zip(list1, list2))
```



This function uses the built-in `zip` function to iterate over the two input lists in parallel, and the `sum` function to count the number of indices where the lists have the same values. The `zip` function returns an iterator of tuples, where each tuple contains one element from each of the input lists. The `sum` function then counts the number of tuples where the elements are equal. This is equivalent to the number of indices where the lists have the same values.

For example, if the input lists are `[1, 2, 3, 4, 5, 6, 7, 8]` and `[2, 2, 3, 1, 2, 6, 7, 9]`, the function will return `4`, because the lists have the same values at indices 0, 2, 4, and 5.