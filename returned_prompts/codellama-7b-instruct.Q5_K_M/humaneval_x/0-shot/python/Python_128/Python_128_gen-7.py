
def prod_signs(arr):
    if not arr: return None
    prod = 1
    for i in arr:
        if i < 0:
            prod *= -1
        elif i > 0:
            prod *= 1
        else:
            prod *= 0
    return sum(abs(i) for i in arr) * prod
