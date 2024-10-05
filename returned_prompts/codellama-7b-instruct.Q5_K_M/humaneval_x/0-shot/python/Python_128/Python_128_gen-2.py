
def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    for a in arr:
        if a == 0:
            prod *= 0
        elif a > 0:
            prod *= 1
        else:
            prod *= -1
    return sum(abs(a) for a in arr) * prod
