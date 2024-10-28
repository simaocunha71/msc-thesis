def is_Monotonic(arr):
    """
    :param arr: array to check
    :return: True if arr is monotonic, False otherwise
    """
    n = len(arr)
    if n <= 1:
        return True
    return all(arr[i] <= arr[i + 1] for i in range(n - 1)) or all(arr[i] >= arr[i + 1] for i in range(n - 1))