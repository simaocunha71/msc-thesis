def max_sub_array_sum(arr: list, max_len: int) -> int:
    if max_len > len(arr):
        max_len = len(arr)
    max_sum = float('-inf')
    current_sum = 0
    for i in range(max_len):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum