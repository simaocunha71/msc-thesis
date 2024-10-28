from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
    # or simply: return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))
    # This is a one-liner version of the function that uses the built-in any() function and a generator expression.
    # It checks if there are any two consecutive elements in the list that are closer than the threshold. If it finds one, it returns True. If it doesn't find any, it returns False.