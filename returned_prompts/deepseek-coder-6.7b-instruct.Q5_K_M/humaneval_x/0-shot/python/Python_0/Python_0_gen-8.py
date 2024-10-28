from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    numbers.sort()
    for i in range(len(numbers)-1):
        if numbers[i+1] - numbers[i] < threshold:
            return True
    return False

print(has_close_elements([1.0, 2.0, 3.0], 0.5))
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

In this code, we first sort the list of numbers in ascending order. Then we iterate over the sorted list and compare the difference between the current number and the next number. If the difference is less than the given threshold, we return True, indicating that there are two numbers closer than the threshold. If we reach the end of the list without finding any two numbers that are closer than the threshold, we return False.

In the example, the first call to the function returns False because there are no two numbers in the list [1.0, 2.0, 3.0] that are closer than 0.5. The second call to the function returns True because there are two numbers in the list [1.0, 2.8, 3.0, 4.0, 5.0, 2.0] that are closer than 0.3.
