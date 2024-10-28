from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_value = min(numbers)
    max_value = max(numbers)

    if min_value == max_value:
        return [0.0] * len(numbers)

    return [(x - min_value) / (max_value - min_value) for x in numbers]

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([-3.0, 0.0, 3.0]))  # Output: [0.0, 0.5, 1.0]  # The list is already rescaled. So, it remains the same.
print(rescale_to_unit([0.0, 0.0, 0.0]))  # Output: [0.0, 0.0, 0.0]  # The list is already rescaled. So, it remains the same.
print(rescale_to_unit([-5.0, -4.0, -3.0, -2.0, -1.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]  # Rescaled list.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled. So, it remains the same.  # The list is already rescaled.