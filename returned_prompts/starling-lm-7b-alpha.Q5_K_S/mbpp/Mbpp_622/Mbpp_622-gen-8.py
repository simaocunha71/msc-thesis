"""
To find the median of two sorted lists of same size, we can follow the below steps:

1. Merge the two sorted lists into one sorted list.
2. Get the middle element of the merged list. If the size of the merged list is even, take the average of the two middle elements.
3. Return the median.

Here is the Python code to implement this:

"""

def merge_sorted_lists(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

def get_median(list1, list2, k):
    merged_list = merge_sorted_lists(list1, list2)
    middle_index = len(merged_list) // 2

    if len(merged_list) % 2 == 0:
        return (merged_list[middle_index - 1] + merged_list[middle_index]) / 2.0
    else:
        return merged_list[middle_index]

# Test the function
list1 = [1, 12, 15, 26, 38]
list2 = [2, 13, 17, 30, 45]
k = 5
print(get_median(list1, list2, k))  # Output: 16.0

"""
This function first merges the two sorted lists into one sorted list using the merge_sorted_lists function. Then, it calculates the median of the merged list using the get_median function. The get_median function takes the merged list and the size of the merged list as input and returns the median.
"""

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

``