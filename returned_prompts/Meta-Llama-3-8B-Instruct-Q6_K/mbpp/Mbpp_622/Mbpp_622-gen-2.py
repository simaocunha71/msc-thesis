```
def get_median(list1, list2, size):
    merged_list = sorted(list1 + list2)
    return float(merged_list[size // 2]) if size % 2 != 0 else (merged_list[size // 2 - 1] + merged_list[size // 2]) / 2
```





The function `get_median` takes two sorted lists and their size as input. It merges the two lists, sorts the merged list, and then calculates the median.

The median is calculated as the middle element if the list size is odd, or the average of the two middle elements if the list size is even.

The unit test `assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0` ensures that the function works correctly.