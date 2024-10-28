
def max_sub_array_sum(arr, n):
    max_sum = -1
    current_sum = 0
    for i in range(0, n):
        current_sum = max(current_sum + arr[i], arr[i])
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


