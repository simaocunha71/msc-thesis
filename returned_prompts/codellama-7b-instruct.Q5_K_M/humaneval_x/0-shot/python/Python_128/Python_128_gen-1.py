
def prod_signs(arr):
    if not arr:
        return None
    sign = 1
    result = 0
    for num in arr:
        result += sign * abs(num)
        sign = -sign
    return result
