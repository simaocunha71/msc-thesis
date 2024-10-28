```
def union_elements(t1, t2):
    return tuple(sorted(set(t1+t2)))
```
The function `union_elements` takes two tuples `t1` and `t2` as input, combines them into a single set, removes duplicates, sorts the set and then converts it back into a tuple. The `assert` statement checks if the output is as expected. 

In this problem, the function `union_elements` finds the union of the elements of two given tuples and outputs them in sorted order. The `set` function is used to remove duplicates and the `sorted` function is used to sort the elements. The `+` operator is used to combine the two tuples into a single set. 

The time complexity of this function is O(n log n) due to the sorting operation, where n is the total number of elements in the two tuples. The space complexity is O(n) for storing the set and the sorted tuple. 