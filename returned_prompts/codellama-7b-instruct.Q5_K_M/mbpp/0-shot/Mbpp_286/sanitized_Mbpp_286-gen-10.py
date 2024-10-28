def max_sub_array_sum_repeated(arr, k, repeated_length):
    return max(sum(arr[i:i+repeated_length]) for i in range(len(arr)-repeated_length+1)) * k