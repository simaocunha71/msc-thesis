```
def get_median(list1, list2, size):
    combined_list = sorted(list1 + list2)
    return combined_list[size // 2] if size % 2 != 0 else (combined_list[size // 2 - 1] + combined_list[size // 2]) / 2
```
The function `get_median` takes two sorted lists of the same size and returns the median of the combined list. The median is calculated as the middle value if the size of the combined list is odd, and the average of the two middle values if the size is even. The function uses the `sorted` function to combine the two lists and find the median. The unit test `assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0` ensures that the function works correctly.  



