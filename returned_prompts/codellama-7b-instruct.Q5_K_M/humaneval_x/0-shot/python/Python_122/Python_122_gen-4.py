
def add_elements(arr, k):
    """
    Time Complexity: O(k)
    Space Complexity: O(1)
    """
    max_num = 10 ** 2
    result = 0
    for i in range(k):
        result += arr[i]
        if result > max_num:
            result = 0
            break
    return result