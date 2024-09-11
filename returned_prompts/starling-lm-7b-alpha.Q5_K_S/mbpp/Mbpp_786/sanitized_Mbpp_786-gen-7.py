def right_insertion(arr, value):
    # Write your code here
    for i in range(len(arr)):
        if value < arr[i]:
            return i
    return len(arr)