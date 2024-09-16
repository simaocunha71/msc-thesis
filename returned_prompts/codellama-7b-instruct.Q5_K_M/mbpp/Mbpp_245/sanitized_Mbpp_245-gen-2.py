def max_sum(arr):
    return max(max_sum_increasing(arr), max_sum_decreasing(arr))
def max_sum_increasing(arr):
    max_sum, current_sum = 0, 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if i == 0 or arr[i] > arr[i-1]:
            if i > 0:
                max_sum = max(max_sum, current_sum)
            else:
                max_sum = current_sum
    return max_sum
def max_sum_decreasing(arr):
    max_sum, current_sum = 0, 0
    for i in range(len(arr)-1, -1, -1):
        current_sum += arr[i]
        if i == len(arr)-1 or arr[i] > arr[i+1]:
            if i < len(arr)-1:
                max_sum = max(max_sum, current_sum)
            else:
                max_sum = current_sum
    return max_sum