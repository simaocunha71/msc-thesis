Here is the Python function to solve the problem:

```Python
def rollingMax(numbers):
    result = []
    max_so_far = float('-inf')
    for num in numbers:
        max_so_far = max(num, max_so_far)
        result.append(max_so_far)
    return result
```

Let's test the function with the given example:

```Python
print(rollingMax([1, 2, 3, 2, 3, 4, 2]))
# Output: [1, 2, 3, 3, 3, 4, 4]
```

The function iterates over the input list and keeps track of the maximum number seen so far. It appends this maximum number to the result list after each iteration. This way, the result list will contain the rolling maximum for each position in the input list.