def prod_signs(arr):
    if len(arr) == 0:
        return -32768
    else:
        return sum(abs(num) * ((-1)**num) for num in arr)

