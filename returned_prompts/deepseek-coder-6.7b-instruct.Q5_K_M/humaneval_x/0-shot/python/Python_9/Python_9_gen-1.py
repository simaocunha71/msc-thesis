Here is a Python solution using a simple loop:

```python
def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    
    result = [numbers[0]]
    
    for i in range(1, len(numbers)):
        result.append(max(numbers[i], result[-1]))
    
    return result
```

This function iterates over the input list. For each number, it appends the maximum between the current number and the last maximum number found so far to the result list. If the input list is empty, it returns an empty list.

Let's test this function with the provided test case:

```python
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This output matches the expected result.

This function runs in O(n) time complexity where n is the size of the input list, as it needs to iterate over the list once. It uses O(n) additional space to store the result list.

Note: This function assumes that the input list is not empty. If the input list can be empty, you should add a check for this case and handle it appropriately.
