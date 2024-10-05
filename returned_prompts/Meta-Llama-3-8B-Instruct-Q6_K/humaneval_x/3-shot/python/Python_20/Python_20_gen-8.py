    min_diff = float('inf')
    closest_pair = None

    for idx, num in enumerate(numbers):
        for idx2, num2 in enumerate(numbers):
            if idx != idx2:
                diff = abs(num - num2)
                if diff < min_diff:
                    min_diff = diff
                    closest_pair = (min(num, num2), max(num, num2))

    return closest_pair


