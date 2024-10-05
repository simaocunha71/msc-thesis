    while True:
        if all(arr[i] >= arr[i+1] for i in range(len(arr)-1)):
            return True
        if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
            return False
        arr.pop(arr.index(max(arr)))
        arr.insert(0, max(arr))


