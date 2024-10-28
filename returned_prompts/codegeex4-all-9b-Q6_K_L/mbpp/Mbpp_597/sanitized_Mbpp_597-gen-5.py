def find_kth(arr1, arr2, k):
    """
    Find kth element from the given two sorted arrays.
    :param arr1: List[int] - first sorted array
    :param arr2: List[int] - second sorted array
    :param k: int - kth element to find
    :return: int - kth element
    """
    i, j = 0, 0
    while i + j < k:
        if i == len(arr1):
            return arr2[j + k - i - 1]
        if j == len(arr2):
            return arr1[i + k - j - 1]
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return min(arr1[i], arr2[j])