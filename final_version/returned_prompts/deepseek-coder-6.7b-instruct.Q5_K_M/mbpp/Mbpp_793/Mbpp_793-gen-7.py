def last(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(last([1,2,3],1))

