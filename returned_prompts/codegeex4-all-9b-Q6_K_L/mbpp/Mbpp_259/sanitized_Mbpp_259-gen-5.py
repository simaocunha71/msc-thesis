def maximize_elements(a, b):
    max_a = max(a, key=lambda x: x[1])
    max_b = max(b, key=lambda x: x[1])
    if max_a[1] > max_b[1]:
        return a
    elif max_a[1] < max_b[1]:
        return b
    else:
        if max_a[0] > max_b[0]:
            return a
        else:
            return b