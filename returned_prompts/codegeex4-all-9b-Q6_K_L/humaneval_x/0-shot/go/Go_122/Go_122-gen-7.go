def add_elements(arr, k):
    if k > len(arr):
        return None

    sum = 0
    for i in range(k):
        num_str = str(arr[i])
        if len(num_str) <= 2:
            sum += arr[i]
    return sum

print(add_elements([111,21,3,4000,5,6,7,8,9], 4))

