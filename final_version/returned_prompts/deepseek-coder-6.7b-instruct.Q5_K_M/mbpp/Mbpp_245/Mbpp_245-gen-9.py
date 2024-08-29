
def max_sum(arr):
    n = len(arr)
    if n < 3:
        return max(arr)

    # max sum of increasing subsequence
    inc = [0]*n
    inc[0] = arr[0]
    for i in range(1, n):
        inc[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]

    # max sum of decreasing subsequence
    dec = [0]*n
    dec[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        dec[i] = arr[i]
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]

    # max sum of bitonic subsequence
    bitonic = [0]*n
    bitonic[0] = inc[0]
    bitonic[-1] = dec[-1]
    for i in range(1, n-1):
        bitonic[i] = max(inc[i], dec[i])
        for j in range(i):
            if arr[i] > arr[j] and bitonic[i] < bitonic[j] + arr[i]:
                bitonic[i] = bitonic[j] + arr[i]

    return max(bitonic)

print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]))  # 194

# the above solution has time complexity O(n^2) and space complexity O(n)


