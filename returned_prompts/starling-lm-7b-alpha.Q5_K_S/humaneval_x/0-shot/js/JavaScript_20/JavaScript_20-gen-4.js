To solve this problem, we can follow these steps:

1. Sort the input array in ascending order. This will allow us to quickly find the two closest elements.
2. Initialize a variable `min_diff` to keep track of the minimum difference between two elements. Set it to positive infinity initially.
3. Initialize two variables `min_num` and `max_num` to keep track of the two closest elements. Set them to the first and last elements of the sorted array.
4. Iterate through the sorted array from index 0 to length - 2. For each element at index `i`, calculate the difference between `min_num` and `max_num`. If this difference is less than `min_diff`, update `min_diff` and `min_num` and `max_num` accordingly.
5. Finally, return the values of `min_num` and `max_num`.

Here's the code implementation:

```python
def findClosestElements(numbers):
    numbers.sort()
    min_diff = float('inf')
    min_num, max_num = numbers[0], numbers[-1]
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < min_diff:
            min_diff = diff
            min_num = numbers[i]
            max_num = numbers[i + 1]
    return min_num, max_num
```

This implementation has a time complexity of O(n), where n is the length of the input array.

To use this function, you can pass in a list of numbers as an argument, like this:

```python
print(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

The function will return the two closest elements in