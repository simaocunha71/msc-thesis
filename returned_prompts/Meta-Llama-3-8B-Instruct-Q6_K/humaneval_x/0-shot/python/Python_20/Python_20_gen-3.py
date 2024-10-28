from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")

    min_diff = float('inf')
    closest_pair = (None, None)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])

    return tuple(sorted(closest_pair))  # return the pair in order


# Testing the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)  # Same number, so same diff
print(find_closest_elements([1.0, 2.0]))  # Expected output: (1.0, 2.0)  # Same for two elements
print(find_closest_elements([1.0]))  # Expected output: ValueError
print(find_closest_elements([]))  # Expected output: ValueError
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]))  # Expected output: (4.0, 5.0)  # Last two elements
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 5.0]))  # Expected output: (4.0, 5.0)  # Last two elements
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 5.0, 5.0]))  # Expected output: (4.0, 5.0)  # Last two elements
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0