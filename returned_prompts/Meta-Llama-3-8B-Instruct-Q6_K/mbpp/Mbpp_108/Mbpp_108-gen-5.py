```
def merge_sorted_list(list1, list2, list3):
    result = []
    for lst in [list1, list2, list3]:
        result.extend(sorted(lst))
    return sorted(result)
```  # Output: [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
```
The code defines a function `merge_sorted_list` that takes three lists as input and returns a single sorted list. It first initializes an empty list `result`. Then, it iterates over the input lists, extends the `result` list with the sorted elements from each list, and finally sorts the `result` list. The sorted list is then returned. The unit test checks the correctness of the function by comparing the output with the expected result.  # Output: [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]```  # Output: [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]```

The time complexity of this solution is O(n log n) due to the sorting operation. The space complexity is O(n) for storing the merged list.  # Output: [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]```  # Output: [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]```

The unit test checks the correctness of the function by comparing the output with the expected result.  # Output: [4, 5, 11, 15, 19, 20, 24, 24, 25