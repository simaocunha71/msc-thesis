from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    return [(num - min_val) / range_val for num in numbers]

print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))

This code finds the minimum and maximum values of the input list, then calculates the range of the list. It then scales each number in the list by subtracting the minimum value from it and dividing by the range, effectively rescaling the list so that the smallest value becomes 0 and the largest value becomes 1.

This code assumes that the input list has at least two elements, as stated in the problem statement. If this assumption is not met, you would need to add error checking to handle cases where the input list has less than two elements.
