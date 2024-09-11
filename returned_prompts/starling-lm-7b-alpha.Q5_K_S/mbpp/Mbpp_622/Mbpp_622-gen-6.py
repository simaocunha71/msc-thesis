To solve this problem, you can follow these steps:

1. Combine the two sorted lists into one.
2. If the length of the combined list is odd, the median is the middle element. If it's even, the median is the average of the two middle elements.
3. Return the median.

Here's an example implementation:

```python
def get_median(list1, list2, size):
    combined_list = list1 + list2
    combined_list.sort()
    if len(combined_list) % 2 == 1:  # Odd length
        return combined_list[len(combined_list) // 2]
    else:  # Even length
        return (combined_list[len(combined_list) // 2 - 1] + combined_list[len(combined_list) // 2]) / 2
```

You can then use this function to find the median of two sorted lists of the same size, as shown in the example test case:

```python
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
```

This assertion should pass, indicating that the function correctly calculates the median of two sorted lists of the same size.

"""

def get_median(list1, list2, size):
    combined_list = list1 + list2
    combined_list.sort()
    if len(combined_list) % 2 == 1:  # Odd length
        return combined_list[len(combined_list) // 2]
    else:  # Even length
        return (combined_list[len(combined_list) // 2 - 1] + combined_list[len(combined_list) // 2]) / 2
```