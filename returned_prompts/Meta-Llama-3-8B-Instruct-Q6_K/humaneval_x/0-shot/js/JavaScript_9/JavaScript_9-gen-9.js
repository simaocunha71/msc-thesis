Here is a Python solution:
```python
def rollingMax(numbers):
    result = []
    max_seen = float('-inf')
    for num in numbers:
        result.append(max(num, max_seen))
        max_seen = num
    return result
```
This function initializes an empty list `result` to store the rolling maximum and a variable `max_seen` to keep track of the maximum value seen so far. It then iterates over the input list `numbers`, updating `max_seen` and `result` for each number. The maximum of the current number and `max_seen` is appended to `result`. Finally, the function returns `result`. The unit test is:
```python
print(rollingMax([1, 2, 3, 2, 3, 4, 2]))  # [1, 2, 3, 3, 3, 4, 4]
```
This function has a time complexity of O(n), where n is the length of the input list, because it makes a single pass over the list. The space complexity is O(n) as well, because it creates a new list to store the result.