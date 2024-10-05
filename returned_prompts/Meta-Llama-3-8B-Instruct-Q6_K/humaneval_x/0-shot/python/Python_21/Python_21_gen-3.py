from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("List should have at least two elements")
    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        return [0.0] * len(numbers)
    return [(x - min_val) / (max_val - min_val) for x in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([1.0, 1.0, 1.0, 1.0, 1.0]))  # Output: [0.0, 0.0, 0.0, 0.0, 0.0] (no change) 
print(rescale_to_unit([-1.0, 1.0]))  # Output: [0.0, 1.0] 
print(rescale_to_unit([0.0, 0.0]))  # Output: [0.0, 0.0] 
print(rescale_to_unit([-10.0, 10.0]))  # Output: [0.0, 1.0] 
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]))  # Output: [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334]
print(rescale_to_unit([1.0, 1.0, 1.0, 1.0, 1.0, 1.0]))  # Output: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] 
print(rescale_to_unit([-5.0, 5.0]))  # Output: [0.0, 1.0] 
print(rescale_to_unit([0.0, 