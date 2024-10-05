    def sign(n):
        if n < 0:
            return -1
        elif n > 0:
            return 1
        else:
            return 0

    if not arr:
        return None

    signs = [sign(n) for n in arr]
    sign_product = 1
    for s in signs:
        sign_product *= s

    return sum(abs(n) for n in arr) * sign_product


