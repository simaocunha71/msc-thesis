```
def get_median(list1, list2, size):
    combined_list = sorted(list1 + list2)
    return combined_list[size // 2] if size % 2 != 0 else (combined_list[size // 2 - 1] + combined_list[size // 2]) / 2
```





