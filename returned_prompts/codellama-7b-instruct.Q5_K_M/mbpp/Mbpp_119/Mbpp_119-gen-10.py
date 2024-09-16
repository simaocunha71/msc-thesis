def search(arr):
    if not arr: return None
    if len(arr) == 1: return arr[0]
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == arr[mid - 1]:
            left = mid + 1
        else:
            right = mid
    return arr[left]

# 3. 
def search(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    if arr[0] != arr[-1]:
        return arr[-1]
    return None

# 4.
def search(arr):
    return next((x for x in arr if arr.count(x) == 1), None)

# 5.
def search(arr):
    for i in range(len(arr)):
        if arr[i] not in arr[i + 1:]:
            return arr[i]
    return None

# 6.
def search(arr):
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            return arr[i]
    return arr[-1]
