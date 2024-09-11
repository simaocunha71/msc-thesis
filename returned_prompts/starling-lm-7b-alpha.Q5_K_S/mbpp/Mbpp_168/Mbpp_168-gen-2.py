```
def frequency(lst, number):
    count = 0
    for i in lst:
        if i == number:
            count += 1
    return count
```

Explanation:
The function `frequency` takes in two parameters: `lst` (the given list) and `number` (the number to count occurrences of). It initializes a variable `count` to 0. Then, it iterates over each element in the list and checks if it is equal to the `number`. If it is, it increments the `count` by 1. Finally, it returns the `count`, which represents the number of occurrences of the `number` in the list.

The provided unit test `assert frequency([1,2,3], 4) == 0` tests the function by passing a list `[1,2,3]` and the number `4`. Since the number 4 is not present in the list, the function should return 0, as expected.

This solution provides a simple and efficient way to count the occurrences of a specific number in a given list using Python.

Here are a few more examples of how you can use the `frequency` function:

```python
print(frequency([1, 2, 3, 4, 4, 4, 5], 4))  # Output: 3
print(frequency([1, 2, 3, 3, 3, 4, 5], 3))  # Output: 3
print(frequency([1, 2, 3, 3, 3, 4, 5], 5))  # Output: 1
print(frequency([1, 2, 3, 3, 3, 4, 5], 6))  # Output: 0
```

These examples demonstrate how the `frequency` function can be used to count the occurrences of a number in a given list, regardless of whether the number is present multiple times or not at all.

By using this function, you can easily determine the frequency of a specific number in a list without having to manually count each occurrence.

This solution is flexible and can be easily adapted to work with different data types, as long as the provided list is iterable