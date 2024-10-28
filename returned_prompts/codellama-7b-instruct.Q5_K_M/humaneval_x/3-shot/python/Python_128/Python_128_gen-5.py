    if not arr:
        return None

    magnitudes = []
    signs = []

    for num in arr:
        if num < 0:
            magnitudes.append(-num)
            signs.append(-1)
        elif num > 0:
            magnitudes.append(num)
            signs.append(1)
        else:
            magnitudes.append(num)
            signs.append(0)

    return sum([magnitude * sign for magnitude, sign in zip(magnitudes, signs)])


