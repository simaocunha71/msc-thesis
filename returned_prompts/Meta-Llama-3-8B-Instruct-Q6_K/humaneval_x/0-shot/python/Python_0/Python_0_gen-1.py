def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([0.1, 0.2, 0.3, 0.4], 0.1))  # True
print(has_close_elements([1.0, 3.0, 5.0], 0.5))  # False
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 1.0))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 2.0))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], 3.0))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], 4.0))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0], 5.0))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], 6.0))  # True
print(has_close_elements([1.0, 2.0, 