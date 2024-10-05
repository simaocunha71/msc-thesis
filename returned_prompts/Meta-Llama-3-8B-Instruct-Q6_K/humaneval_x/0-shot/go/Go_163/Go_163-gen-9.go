    return sorted(set(l1) & set(l2))



Here is the explanation of the provided code:

The function `common` takes two lists `l1` and `l2` as input and returns a sorted list of unique common elements.

The function uses the `set` function to convert the lists to sets. The `&` operator is then used to get the intersection of the two sets, which is a set of common elements. The `set` function is used again to convert the set back to a list, and finally the `sorted` function is used to sort the list.

The provided unit tests demonstrate the functionality of the function. For example, the test `common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])` checks that the function returns the sorted unique common elements `[1, 5, 653]`. Similarly, the test `common([5, 3, 2, 8], [3, 2])` checks that the function returns the sorted unique common elements `[2, 3]`.