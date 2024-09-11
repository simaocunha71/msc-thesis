```
def frequency(lst, num):
    '''This function counts the number of occurrences of a number in a list.'''
    count = 0
    for i in lst:
        if i == num:
            count += 1
    return count
```

Here is the step-by-step explanation:

1. Define the function `frequency` that takes two parameters: `lst` and `num`.
2. Initialize a counter `count` to 0. This counter will keep track of the number of occurrences of `num` in the `lst`.
3. Loop through the `lst` using a `for` loop. For each element `i` in the `lst`, check if it is equal to `num`.
4. If `i` is equal to `num`, increment the `count` by 1.
5. After the loop is finished, return the `count`.

To test this function, you can use the `assert` statement to check if the function returns the correct value for a given input. For example, if you call `frequency([1,2,3], 4)`, it should return 0 because there are no occurrences of 4 in the list.

Here's an example of how you can use the `frequency` function:

```python
numbers = [1, 2, 3, 4, 3, 2, 1, 3, 3, 3]
frequency = frequency(numbers, 3)  # returns 3
```

In this example, the `numbers` list contains 3 occurrences of the number 3, so the `frequency` function will return 3.

```python
frequency = frequency([1,2,3], 4)  # returns 0
```

In this example, the `frequency` function will return 0 because there are no occurrences of the number 4 in the list `[1,2,3]`.

```python
frequency = frequency([1,2,3], 1)  # returns 1
```

In this example, the `frequency` function will return 1 because the number 1 appears once in the list `[1,2,3]`.

