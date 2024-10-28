To generate a list of rolling maximum element until given moment in the sequence, you can use the following code:

```python
def rollingMax(numbers):
    max_list = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > max_list[i-1]:
            max_list.append(numbers[i])
        else:
            max_list.append(max_list[i-1])
    return max_list
```

The `rollingMax` function takes a list of integers called `numbers` as input. It initializes the `max_list` with the first element of the input list. Then, it iterates through the remaining elements of the input list using a for loop. For each element, it compares it with the previous maximum value in the `max_list`. If the current element is greater than the previous maximum, it appends the current element to the `max_list`. Otherwise, it appends the previous maximum value. Finally, it returns the `max_list` which contains the rolling maximum elements until the given moment in the sequence.

For example, if you call `rollingMax([1, 2, 3, 2, 3, 4, 2])`, it will return `[1, 2, 3, 3, 3, 4, 4]`.

This solution ensures that the maximum value is always included in the `max_list`, and if the current element is not greater than the previous maximum, it keeps the previous maximum value in the list.

Hope this helps!

Note: The code provided is in Python, but the concept can be applied to other programming languages as well.

Here are some additional examples of how you can use the `rollingMax` function:

- `rollingMax([1, 4, 3, 2, 4, 1])` will return `[1, 4, 4, 4, 4, 4]`
- `rollingMax([2, 3, 4, 2, 5, 1])` will return `[2, 3, 4, 4, 5, 5]`
- `rollingMax([10, 20,