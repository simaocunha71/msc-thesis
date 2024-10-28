def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    min_difference = float('inf')
    result = (0, 0)
    for i in range(len(numbers) - 1):
        difference = numbers[i + 1] - numbers[i]
        if difference < min_difference:
            min_difference = difference
            result = (numbers[i], numbers[i + 1])
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

