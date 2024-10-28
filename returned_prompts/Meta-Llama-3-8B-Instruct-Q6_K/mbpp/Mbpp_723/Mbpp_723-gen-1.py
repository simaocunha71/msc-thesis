```
def count_same_pair(list1, list2):
    return sum(1 for a, b in zip(list1, list2) if a == b)
```


This function uses the built-in zip function to iterate over the two lists in parallel. The sum function then adds up the number of times the corresponding elements are equal. The lambda function inside the sum function is a generator expression that yields 1 for each pair of equal elements and 0 for each pair of unequal elements. The sum of these 1s and 0s gives the total count of indices where the lists have the same values. The unit test provided ensures that this function works correctly. 





The unit test provided is:
```
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
```

This test case checks if the function correctly counts the indices where the lists have the same values. The expected output is 4, which means the function should return 4 when the input lists are [1, 2, 3, 4, 5, 6, 7, 8] and [2, 2, 3, 1, 2, 6, 7, 9].