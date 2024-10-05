    if len(arr) < k:
        raise ValueError("k is larger than the length of the array")

    sum = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum += arr[i]

    return sum

