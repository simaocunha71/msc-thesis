
def max_sub_array_sum_repeated(arr: list, k: int, n: int) -> int:
    total_sum = sum(arr)
    max_sum = curr_sum = sum(arr[:n])
    for i in range(n, k*n):
        curr_sum += arr[i%n] - arr[i-n]
        max_sum = max(max_sum, curr_sum)
    return max_sum if max_sum >=0 else max_sum + ((k-1)*total_sum)


