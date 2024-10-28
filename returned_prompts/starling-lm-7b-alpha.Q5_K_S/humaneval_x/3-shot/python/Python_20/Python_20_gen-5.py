    min_diff = min(abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1))
    closest_elems = (numbers[i] for i in range(len(numbers)) if abs(numbers[i] - numbers[i + 1]) == min_diff)

    return next(closest_elems), next(closest_elems)


