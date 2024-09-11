def is_majority(arr, n, element):
    cnt = 0
    for i in range(n):
        if arr[i] == element:
            cnt += 1
    return cnt > n // 2


def is_majority(arr, n, element):
    cnt = 0
    left = 0
    right = n - 1
    while left < right:
        if arr[left] == arr[right] == element:
            left += 1
        elif arr[left] == element:
            cnt += 1
            left += 1
        elif arr[right] == element:
            cnt += 1
            right -= 1
        else:
            return False
    return cnt > n // 2


print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))
print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 2))
# 返回True 返回False
"""
def is_majority(arr, n, element):
    cnt = 0
    left = 0
    right = n - 1
    while left < right:
        if arr[left] == arr[right] == element:
            left += 1
        elif arr[left] == element:
            cnt += 1
            left += 1
        elif arr[right] == element:
            cnt += 1
            right -= 1
        else:
            return False
    return cnt > n // 2
"""

def is_majority(arr, n, element):
    cnt = 0
    for i in range(n):
        if arr[i] == element:
            cnt += 1
    return cnt > n // 2


# print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))
# print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 2))