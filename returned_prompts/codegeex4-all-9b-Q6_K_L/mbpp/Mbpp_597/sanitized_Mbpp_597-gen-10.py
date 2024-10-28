def find_kth(arr1, arr2, k):
    """
    Find kth element from the given two sorted arrays.

    :param arr1: First sorted array
    :param arr2: Second sorted array
    :param k: kth element to find
    :return: kth element
    """
    if k < 1 or k > len(arr1) + len(arr2):
        raise ValueError("Invalid value of k")

    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if i + 1 == k:
                return arr1[i]
            i += 1
        else:
            if j + 1 == k:
                return arr2[j]
            j += 1

    if i < len(arr1):
        return arr1[i + k - 1]
    else:
        return arr2[j + k - 1]