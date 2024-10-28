    n = len(arr)
    if n == 0:
        return True
    if n == 1:
        return True
    if n == 2:
        return arr[0] < arr[1]

    max_element = max(arr)
    min_element = min(arr)

    if arr.index(max_element) < n - 1 and arr[arr.index(max_element) + 1] == min_element:
        return False
    if arr.index(min_element) > 0 and arr[arr.index(min_element) - 1] == max_element:
        return False

    return True


