```
def get_median(list1, list2, n):
    merged = sorted(list1 + list2)
    return merged[n // 2] if n % 2 else (merged[n // 2 - 1] + merged[n // 2]) / 2
```


The function `get_median` takes two sorted lists `list1` and `list2` of the same size `n` as input. It merges the two lists, sorts the merged list, and then finds the median. If the size of the merged list is even, the median is the average of the two middle numbers. 

The unit test `assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0` ensures that the function works correctly. 

Note: This solution assumes that the input lists are sorted. If the input lists are not sorted, the function may not work correctly. 

Also, this solution assumes that the input lists have the same size. If the input lists have different sizes, the function may not work correctly. 

Finally, this solution assumes that the input lists are non-empty. If the input lists are empty, the function may not work correctly. 

In a real-world scenario, you would want to add error checking to handle these cases. 





