from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True

# Test case with negative numbers
print(has_close_elements([-1.0, 0.0, 1.0], 0.5))  # False
print(has_close_elements([-2.0, -1.5, -1.0, 0.0], 0.5))  # True
# Test case with decimal numbers
print(has_close_elements([1.5, 2.5, 3.5], 0.5))  # True
print(has_close_elements([1.5, 3.5, 5.5], 0.5))  # False
# Test case with duplicate numbers
print(has_close_elements([1.0, 2.0, 2.0, 3.0], 0.5))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0], 0.5))  # False
# Test case with very close numbers
print(has_close_elements([1.0, 1.00001, 1.00002], 0.5))  # True
print(has_close_elements([1.0, 1.5, 2.0], 0.5))  # False
# Test case with single number
print(has_close_elements([1.0], 0.5))  # False
print(has_close_elements([1.0, 1.0], 0.5))  # True
# Test case with empty list
print(has_close_elements([], 0.5))  # False
# Test case with single element list
print(has_close_elements([1.0], 0.5))  # False
print(has_close_elements([1.0,