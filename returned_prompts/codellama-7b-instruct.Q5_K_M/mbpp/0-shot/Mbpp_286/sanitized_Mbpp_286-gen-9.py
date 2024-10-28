def max_sub_array_sum_repeated(arr, k, n):
    # Find the maximum sum subarray of arr[0..n-1]
    max_sum = 0
    current_sum = 0
    for i in range(n):
        current_sum = current_sum + arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    # Repeat the given array k times and then find the maximum sum subarray of the modified array
    max_sum_repeated = 0
    current_sum = 0
    for i in range(n):
        for j in range(k):
            current_sum = current_sum + arr[i]
            if current_sum > max_sum_repeated:
                max_sum_repeated = current_sum
            elif current_sum < 0:
                current_sum = 0
    return max_sum_repeated