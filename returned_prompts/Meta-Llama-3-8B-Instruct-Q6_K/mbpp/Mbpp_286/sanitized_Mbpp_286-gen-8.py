def max_sub_array_sum_repeated(arr, k, n):
    max_sum = float('-inf')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            total = 0
            for x in range(k):
                for num in arr[i:j+1]:
                    total += num
            max_sum = max(max_sum, total)
    return max_sum