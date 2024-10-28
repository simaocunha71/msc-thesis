"""
def kth_element(arr, k):
    # check if the input is valid
    if k < 1 or k > len(arr):
        raise ValueError("k should be between 1 and the length of the array")
    # find the kth element
    return sorted(arr)[k - 1]
"""
