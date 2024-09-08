def odd_length_sum(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray = arr[i:j+1]
            if len(subarray) % 2 != 0:
                total += sum(subarray)
    return total