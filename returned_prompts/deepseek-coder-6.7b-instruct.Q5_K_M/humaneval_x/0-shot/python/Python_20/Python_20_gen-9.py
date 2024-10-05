def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    min_diff = float('inf')
    result = (0, 0)
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i-1], numbers[i])
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

This function first sorts the list of numbers. It then iterates through the sorted list, comparing each number with the previous one. If the difference (which represents the 'distance') is less than the minimum difference found so far, it updates the minimum difference and the pair of numbers that form that difference. In the end, it returns the pair of numbers that form the smallest difference.

This solution has a time complexity of O(n log n) due to the sorting, where n is the length of the input list.
"""

#