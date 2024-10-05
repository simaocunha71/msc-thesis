
def prod_signs(arr):
    if not arr:
        return None
    product = 1
    for x in arr:
        product *= x
    return sum(abs(x) for x in arr) * product
