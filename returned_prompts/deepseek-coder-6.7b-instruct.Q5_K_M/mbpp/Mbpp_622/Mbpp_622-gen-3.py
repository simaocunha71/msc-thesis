"""
The function first merges the two lists into one sorted list. Then it finds the median of the merged list.

Here is the python code for the above problem:

```python
def merge_lists(list1, list2):
    return sorted(list1 + list2)

def get_median(list1, list2, n):
    merged_list = merge_lists(list1, list2)
    
    if n % 2 != 0:
        return merged_list[n // 2]
    else:
        return (merged_list[n // 2 - 1] + merged_list[n // 2]) / 2.0
```

In the above code, 'merge_lists' function merges two sorted lists and returns a sorted list. 'get_median' function takes two sorted lists and the size of the lists as input and returns the median of the merged list.

Here, we first merge the two lists. If the size of the merged list is odd, the median is the middle element. If the size of the merged list is even, the median is the average of the two middle elements.
"""

