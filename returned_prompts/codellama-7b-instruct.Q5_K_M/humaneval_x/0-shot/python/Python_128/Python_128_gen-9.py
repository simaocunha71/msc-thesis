
def prod_signs(arr):
    if not arr:
        return None

    signs = [1, -1, 1]
    s = 0
    for i in arr:
        s += signs[i % 3] * abs(i)
    return s
