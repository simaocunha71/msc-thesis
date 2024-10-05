from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    min_diff = float('inf')
    closest_pair = ()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])
    return closest_pair

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
print(find_closest_elements(numbers))  # Output: (2.0, 2.2)

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
print(find_closest_elements(numbers))  # Output: (2.0, 2.0)
```

The function `find_closest_elements` iterates over all pairs of numbers in the list and keeps track of the pair with the smallest difference between its elements. It returns the pair with the smallest difference. If there are multiple such pairs, it returns the first one it finds. The function does not assume that the input list contains at least two distinct numbers. It returns a tuple of two numbers, which are the closest to each other. If the input list contains less than two distinct numbers, the function returns a tuple with the same number repeated twice.

The function is implemented in a way that it can be used with lists of any length. It does not assume that the list is sorted or has any specific properties. It simply iterates over all pairs of numbers in the list and keeps track of the pair with the smallest difference between its elements.

The time complexity of this function is O(n^2), where n is the length of the input list. This is because the function iterates over all pairs of numbers in the list, which takes O(n^2) time. The space complexity is O(1), because the function uses a constant amount of space to store the result and the minimum difference. 

The function is tested with two example inputs. The first input is a list of six numbers, and the output is `(2.0, 2.2)`, which are the closest numbers to each other in the list. The second input is a list of six numbers, and the output