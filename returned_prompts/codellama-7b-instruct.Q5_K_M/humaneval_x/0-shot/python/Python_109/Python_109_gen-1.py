
def move_one_ball(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    if not arr:
        return True
    arr = sorted(arr, reverse=True)
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True