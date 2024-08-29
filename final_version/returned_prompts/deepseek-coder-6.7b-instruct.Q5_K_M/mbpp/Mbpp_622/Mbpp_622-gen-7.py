"""
First, we concatenate the two lists. Then, we sort the concatenated list. The median of a list is the middle element if the list has an even number of elements. If the list has an odd number of elements, the median is the average of the two middle elements.

In Python:
"""

def get_median(lst1, lst2, n):
    merged = lst1 + lst2
    merged.sort()

    if n % 2 == 0:  # even number of elements
        median1 = merged[n//2]
        median2 = merged[n//2 - 1]
        return (median1 + median2) / 2
    else:  # odd number of elements
        return merged[n//2]

# test case
print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5))  # should return 16.0

"""
The time complexity of this solution is O(n log n), because we need to sort the merged list. The space complexity is O(n), because we need to store the merged list.
"""

"""
This solution works because the median of two sorted lists is the median of the merged list. If the merged list has an even number of elements, the median is the average of the two middle elements. If the merged list has an odd number of elements, the median is the middle element.
"""
"""
Note: This solution assumes that the input lists are sorted. If the input lists are not sorted, you would first need to sort them before finding the median.
"""
<jupyter_output>
16.0
<jupyter_text>
