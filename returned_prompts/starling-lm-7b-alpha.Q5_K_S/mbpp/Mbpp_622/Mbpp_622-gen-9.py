"""
Here is a Python solution that uses the bisect module to achieve this:

```python
from bisect import bisect_left

def get_median(l1, l2, k):
    """
    Get the median of two sorted lists of same size.

    Parameters:
    l1 (list): the first sorted list of integers
    l2 (list): the second sorted list of integers
    k (int): the size of the two lists

    Returns:
    float: the median
    """
    merged_list = sorted(l1 + l2)
    index = bisect_left(merged_list, merged_list[k])
    return merged_list[index]
```

This function works by first merging the two lists into a single sorted list. It then uses the `bisect_left` function to find the index at which the kth value in the merged list is located. This index is then used to return the value at that index, which is the median of the two original lists.
"""

# Python3 code to get median of two sorted arrays 

# Function to get median of two sorted arrays 
def getMedian(a, b, n): 
    c = a + b 
    d = sorted(c) 

    # if size of merged array is odd 
    if (n % 2 == 1): 
        return d[n // 2] 

    # if size of merged array is even 
    else: 
        return (d[n // 2 - 1] + d[n // 2]) / 2.0

# Driver Code 
a = [1, 12, 15, 26, 38] 
b = [2, 13, 17, 30, 45] 
n = len(a) 

print(getMedian(a, b, n))


"""
The getMedian function takes in two sorted lists, a and b, and the size of the lists, n. It merges the two lists into a single list, c, and then sorts the merged list. If the size of the merged list is odd, it returns the middle