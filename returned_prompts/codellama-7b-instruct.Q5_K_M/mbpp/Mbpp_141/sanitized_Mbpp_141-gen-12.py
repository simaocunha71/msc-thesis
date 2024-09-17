def pancake_sort(arr):
    for i in range(len(arr)-1,0,-1):
        max_idx = arr[0:i].index(max(arr[0:i]))
        flipped = arr[0:i][::-1]
        arr = flipped[max_idx:]+flipped[:max_idx]+arr[i:]
    return arr