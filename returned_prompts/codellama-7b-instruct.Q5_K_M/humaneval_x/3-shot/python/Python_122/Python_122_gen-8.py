    # O(n) time, O(n) space
    arr.sort()
    result = 0
    for i in range(k):
        result += arr[i]
    return result


