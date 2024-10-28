```
def count_same_pair(list1, list2):
    return sum(i == j for i, j in zip(list1, list2))
```
This function uses the built-in `zip` function to iterate over the two lists in parallel. It then uses a generator expression to compare each pair of elements and sum up the number of pairs that are equal.

For example, if the input lists are `[1, 2, 3, 4, 5, 6, 7, 8]` and `[2, 2, 3, 1, 2, 6, 7, 9]`, the function will return `4`, which is the number of indices where the lists have the same values (at indices 1, 2, 5, and 6).