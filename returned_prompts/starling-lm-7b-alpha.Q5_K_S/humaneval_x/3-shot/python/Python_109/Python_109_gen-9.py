    def check(arr):
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True

    def move(arr):
        arr.append(arr[0])
        del arr[0]
        return arr

    if len(arr) == 0:
        return True

    for i in range(n):
        if arr[i] < arr[i+1]:
            return check(move(arr))
    return True



