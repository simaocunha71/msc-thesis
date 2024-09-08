def last(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
    return -1

print(last([1,2,3],1))  # 0

