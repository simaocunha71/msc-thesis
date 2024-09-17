def max_sub_array_sum_repeated(arr, k, m):
    arr.extend(arr[:])
    arr.extend(arr[:])
    arr.extend(arr[:])
    arr.extend(arr[:])
    return max(sum(arr[i:i+m]) for i in range(len(arr)-m+1))