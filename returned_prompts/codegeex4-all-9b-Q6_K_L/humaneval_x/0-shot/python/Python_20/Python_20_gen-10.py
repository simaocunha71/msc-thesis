```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers")
    
    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[0] - numbers[1])
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])
    
    return closest_pair
```

The `find_closest_elements` function first checks if the list has at least two numbers. If not, it raises a `ValueError`. Then it initializes the closest pair to the first two numbers and the minimum difference to their absolute difference. It then iterates through the list, comparing each pair of numbers and updating the closest pair and minimum difference if a smaller difference is found. Finally, it returns the closest pair of numbers.