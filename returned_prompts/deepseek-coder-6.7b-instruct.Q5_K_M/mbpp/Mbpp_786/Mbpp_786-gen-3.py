def right_insertion(arr, val):
    for i in range(len(arr)):
        if arr[i] > val:
            return i
    return len(arr)

print(right_insertion([1,2,4,5],6))

