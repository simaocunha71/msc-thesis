from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] < threshold:
            return True
    return False

print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True

The above function works by first sorting the list of numbers. Then it goes through the sorted list of numbers and checks if the difference between any two consecutive numbers is less than the threshold. If it finds such pair, it returns True. If it doesn't find any such pair after checking all the numbers, it returns False.
"""


"""
