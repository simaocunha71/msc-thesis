"""
def get_median(list1, list2, size):
    # Calculate the median of two sorted lists of same size.
    # The median is the middle value in the list. If the size of the list is odd,
    # the median is the middle value. If the size is even, the median is average of the two middle values.
    if size % 2 == 0:
        return (list1[size//2] + list2[size//2])/2
    else:
        return list1[size//2]
"""