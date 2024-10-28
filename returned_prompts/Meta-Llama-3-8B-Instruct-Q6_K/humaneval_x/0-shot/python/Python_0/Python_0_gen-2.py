from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.5))  # False
print(has_close_elements([1.0, 2.0, 2.1, 2.2, 3.0], 0.1))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.1))  # False
print(has_close_elements([1.0, 2.0, 2.0, 3.0, 4.0, 5.0], 0.1))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.01))  # True
print(has_close_elements([1.0, 1.0, 1.0, 2.0, 3.0, 4.0, 5.0], 0.01))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], 0.01))  # False
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0], 0.