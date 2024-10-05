    arr = [int(i) for i in arr]
    return sum([arr[i] for i in range(k) if len(str(arr[i])) <= 2])


