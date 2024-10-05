from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = float('-inf')
    result = []
    for num in numbers:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    return result

print(rolling_max([1, 2, 3, 2, 3, 4, 2]))

Output:
[1, 2, 3, 3, 3, 4, 4]

This function works by iterating over the input list of integers and updating the maximum value found so far (`max_so_far`) whenever a new maximum is found. The current maximum is then appended to the result list. The function finally returns the result list.

The time complexity of this solution is O(n) as it makes a single pass over the input list, and the space complexity is also O(n) as it stores the result in a new list.

I hope this helps. Let me know if you have any other questions.


A: You can try this.
def rolling_max(numbers):
    max_val = float('-inf')
    result = []
    for num in numbers:
        max_val = max(max_val, num)
        result.append(max_val)
    return result

This function works by initializing max_val as negative infinity and result as an empty list. It then iterates over the numbers in the input list. For each number, it updates max_val to be the maximum of the current number and the previous max_val, and appends the new max_val to the result list. The function then returns the result list.

A: You can also use Python's map function in combination with the built-in max function to achieve the same result:

```python
def rolling_max(numbers):
    return list(map(max, numbers, [0] + numbers))
```

This function works by creating a new list where each element is the maximum of the current element and the previous maximum. The previous maximum is obtained by concatenating the input list with itself, shifted one element to the right