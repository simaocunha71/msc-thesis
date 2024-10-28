def add_elements(arr, k):
    total = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            total += arr[i]
    return total

print(add_elements([111,21,3,4000,5,6,7,8,9], 4)) # Output: 24