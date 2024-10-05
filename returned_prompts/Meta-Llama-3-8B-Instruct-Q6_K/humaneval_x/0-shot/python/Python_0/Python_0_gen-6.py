def has_close_elements(numbers: List[float], threshold: float) -> bool:
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] <= threshold:
            return True
    return False
    # This function first sorts the list of numbers.
    # Then it iterates over the list, checking each pair of adjacent numbers.
    # If it finds a pair whose difference is less than or equal to the threshold,
    # it returns True. If it doesn't find any such pair, it returns False.