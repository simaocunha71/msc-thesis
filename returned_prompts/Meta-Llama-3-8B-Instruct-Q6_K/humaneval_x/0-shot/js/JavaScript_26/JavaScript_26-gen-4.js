Here is a Python solution that uses a dictionary to keep track of the elements that have been seen before:

```python
def removeDuplicates(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```
In this solution, we iterate over the input list. For each number, we check if it has been seen before by checking if it is in the `seen` set. If it hasn't been seen before, we add it to the `seen` set and to the `result` list. Finally, we return the `result` list.

For example, if we call `removeDuplicates([1, 2, 3, 2, 4])`, the function will return `[1, 3, 4]`. The `seen` set will be `{1, 2, 3, 4}` after the function has finished running.

This solution has a time complexity of O(n), where n is the length of the input list, because we only iterate over the input list once. The space complexity is also O(n), because in the worst case, we might need to store all elements in the `seen` set. However, in practice, the space complexity is usually much smaller because we typically don't have a lot of duplicate elements in a list.