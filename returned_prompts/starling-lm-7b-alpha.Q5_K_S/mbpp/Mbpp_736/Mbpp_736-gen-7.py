def left_insertion(arr, value):
    """
    Time: O(log n)
    Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    mid = 0
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return mid


def left_insertion_v2(arr, value):
    """
    Time: O(n)
    Space: O(1)
    """
    i = 0
    while i < len(arr) and value <= arr[i]:
        i += 1
    return i


def left_insertion_v3(arr, value):
    """
    Time: O(n)
    Space: O(1)
    """
    for i in range(len(arr)):
        if value < arr[i]:
            return i
    return len(arr)


if __name__ == "__main__":
    assert left_insertion([1, 2, 4, 5], 6) == 4
    assert left_insertion_v2([1, 2, 4, 5], 6) == 4
    assert left_insertion_v3([1, 2, 4, 5], 6) == 4
    assert left_insertion([], 1) == 0
    assert left_insertion_v2([], 1) == 0
    assert left_insertion_v3([], 1) == 0
    assert left_insertion([1], 0) == 0
    assert left_insertion_v2([1], 0) == 0
    assert left_insertion_v3([1], 0) == 0
    assert left_insertion([1, 2], 0) == 0
    assert left_insertion_v2([1, 2], 0) == 0
    assert left_insertion_v3([1, 2], 0) == 1
