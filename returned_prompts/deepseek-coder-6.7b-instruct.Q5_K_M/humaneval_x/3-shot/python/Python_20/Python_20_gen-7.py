    numbers.sort()
    min_diff  , min_pair = float('inf'), (None, None)

    for idx in range(1, len(numbers)):
        diff = numbers[idx]  - numbers[idx  - 1]
        if diff < min_diff:
            min_diff = diff
            min_pair = (numbers[idx  - 1], numbers[idx])

    return min_pair


