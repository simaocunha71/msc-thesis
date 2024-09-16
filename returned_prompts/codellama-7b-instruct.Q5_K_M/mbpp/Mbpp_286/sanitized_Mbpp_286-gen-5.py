def max_sub_array_sum_repeated(arr, k, repetitions):
    # Write your code here
    return max(
        sum(arr[i:j])
        for i in range(k * repetitions)
        for j in range(i + 1, k * repetitions + 1)
    )