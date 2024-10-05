    if not arr:
        return None

    signs = [1 if num > 0 else -1 for num in arr]
    magnitudes = [abs(num) for num in arr]

    return sum(magnitudes) * prod(signs)


def prod(arr):
    result = 1
    for num in arr:
        result *= num
    return result

