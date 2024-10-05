    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False


# Some tests
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.5))  # False
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.3))  # True


# More tests
print(has_close_elements([-3, 3, 4, 5, 6], 0.5))  # False
print(has_close_elements([-3, 3, 4, 5, 6], 0.3))  # True
print(has_close_elements([-3, -2, -1, 0, 1, 2, 3], 0.5))  # False
print(has_close_elements([-3, -2, -1, 0, 1, 2, 3], 0.3))  # True


# More tests
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], 0.5))  # False
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], 0.3))  # True
print(has_close_elements([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 