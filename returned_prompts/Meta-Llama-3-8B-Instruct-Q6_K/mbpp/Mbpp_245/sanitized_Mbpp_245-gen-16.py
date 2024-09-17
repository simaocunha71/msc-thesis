def max_sum(arr):
    n = len(arr)
    inc = [0] * n
    dec = [0] * n

    inc[0] = arr[0]
    dec[0] = arr[0]

    for i in range(1, n):
        if arr[i] > inc[i-1]:
            inc[i] = arr[i] + inc[i-1]
        else:
            inc[i] = inc[i-1]

        if arr[i] > dec[i-1]:
            dec[i] = arr[i] + dec[i-1]
        else:
            dec[i] = dec[i-1]

    return max(max(inc), max(dec))