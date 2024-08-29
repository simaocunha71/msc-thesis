def right_insertion(arr, target):
    for i in range(len(arr)):
        if arr[i] > target:
            return i
    return len(arr)

print(right_insertion([1,2,4,5],6)) # 4

