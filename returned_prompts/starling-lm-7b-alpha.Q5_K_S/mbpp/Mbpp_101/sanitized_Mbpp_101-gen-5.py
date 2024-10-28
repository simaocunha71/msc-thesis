def kth_element(nums, k):
    """
    Parameters:
    nums: a list of integers
    k: the kth element in the array
    Returns:
    the kth element in the array
    """
    return sorted(nums)[k-1]