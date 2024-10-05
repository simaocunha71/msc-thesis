```python
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()  # Sort the list in ascending order
    min_diff = float('inf')  # Initialize min_diff as infinity
    closest_pair = (None, None)  # Initialize closest_pair as a tuple of two None values

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]  # Calculate the difference between consecutive elements
        if diff < min_diff:  # If the difference is smaller than min_diff
            min_diff = diff  # Update min_diff
            closest_pair = (numbers[i], numbers[i + 1])  # Update closest_pair

    return closest_pair  # Return the closest pair of elements
```