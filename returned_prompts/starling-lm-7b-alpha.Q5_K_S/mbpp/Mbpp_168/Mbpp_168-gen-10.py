```
def frequency(list1, number):
    counter = 0
    for i in list1:
        if i == number:
            counter += 1
    return counter
```

Explanation:

The function `frequency` takes two parameters: `list1` and `number`. It initializes a counter variable to 0. Then, it iterates through each element in `list1` using a `for` loop. If an element is equal to `number`, the counter is incremented by 1. Finally, the function returns the value of the counter, which represents the number of occurrences of `number` in `list1`.

The provided `assert` statement checks if the function correctly returns 0 when given an empty list and a number. This ensures that the function is working as expected.

To use the function, you can call it with the desired list and number as arguments. For example, `frequency([1, 2, 3], 4)` will return 0, as there are no occurrences of 4 in the given list.

Overall, this function provides a way to count the number of occurrences of a specific number in a given list using a simple and efficient approach.

```python
def frequency(list1, number):
    counter = 0
    for i in list1:
        if i == number:
            counter += 1
    return counter
```

This function iterates through each element in the `list1` and checks if it is equal to the `number`. If a match is found, the counter is incremented by 1. Finally, the function returns the value of the counter, which represents the number of occurrences of the `number` in the `list1`.

For example, if you call `frequency([1, 2, 3], 4)`, it will return 0, as there are no occurrences of 4 in the given list.

The function is implemented in a straightforward manner, making it easy to understand and use. It provides a reliable way to count the occurrences of a specific number in a given list.

To use this function, you can call it with the desired list and number as arguments. For example, `frequency([1, 2, 3], 4)`