
def prod_signs(arr):
    prod = 1
    sign = 1
    for i in arr:
        prod *= sign
        if i == 0:
            sign = 0
        elif i > 0:
            sign = 1
        else:
            sign = -1
    return prod * sum(abs(i) for i in arr) if arr else None
