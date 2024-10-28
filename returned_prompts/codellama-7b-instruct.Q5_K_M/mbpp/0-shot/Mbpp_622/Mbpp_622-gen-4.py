"""
def get_median(list1, list2):
    # Find the middle index
    mid = len(list1) // 2

    # Find the middle index in the other list
    other_mid = len(list2) // 2

    # Check if the lengths are odd or even
    if len(list1) % 2 == 0:
        # If they are even, then we want to find the average of the two elements in the middle
        return (list1[mid] + list2[other_mid]) / 2
    else:
        # If they are odd, then we want to return the middle element
        return list1[mid]
"""
