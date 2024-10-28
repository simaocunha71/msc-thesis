def has_close_elements(numbers: List[float], threshold: float) -> bool:
    numbers.sort()
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] < threshold:
            return True
    return False


print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True

This code works by sorting the input list of numbers, then iterating through the list, comparing each number to its previous one. If the difference is less than the given threshold, the function immediately returns True. If the function iterates through the entire list without finding a pair of numbers that are closer than the given threshold, it returns False.
'''

#Exercise 3
'''
