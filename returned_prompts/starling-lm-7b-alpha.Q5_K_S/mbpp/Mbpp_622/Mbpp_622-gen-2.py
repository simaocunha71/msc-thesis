"""
Here's a solution to find the median of two sorted lists of same size:

```python
def get_median(list1, list2, n):
    # Create a list with both lists
    combined_list = list1 + list2
    # Sort the combined list
    combined_list.sort()
    # Calculate the index of the median element
    median_index = n // 2
    # Check if the median is in the first half or the second half of the combined list
    if median_index < len(combined_list) // 2:
        median = combined_list[median_index]
    else:
        median = combined_list[-median_index-1]
    # Return the median
    return median
```

You can test the function with the given assertion:

```python
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
```
"""

def get_median(list1, list2, n):
    # Create a list with both lists
    combined_list = list1 + list2
    # Sort the combined list
    combined_list.sort()
    # Calculate the index of the median element
    median_index = n // 2
    # Check if the median is in the first half or the second half of the combined list
    if median_index < len(combined_list) // 2:
        median = combined_list[median_index]
    else:
        median = combined_list[-median_index-1]
    # Return the median
    return median

assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0



```  
```

```python
def get_median(list1, list2, n):
    # Create a list with both lists
    combined_list = list1 + list2
   