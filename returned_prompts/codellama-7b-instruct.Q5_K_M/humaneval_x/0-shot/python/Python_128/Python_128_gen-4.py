
def prod_signs(arr):
    if len(arr) == 0:
        return None
    else:
        prod = 1
        for i in range(len(arr)):
            if arr[i] > 0:
                prod *= 1
            elif arr[i] < 0:
                prod *= -1
            else:
                prod *= 0
        return prod





