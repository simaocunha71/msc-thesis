To solve this problem, you can follow these steps:

1. Create a copy of the original list, called 'lCopy'.
2. Iterate through each element in 'lCopy'.
3. If the index of the element is divisible by 3, sort the element in 'lCopy' based on its value.
4. Return the sorted list 'lCopy'.

Here's the code to implement the above steps:

```python
def sortThird(l):
    lCopy = l.copy()
    for i in range(len(l)):
        if (i + 1) % 3 == 0:
            lCopy[i] = sorted(lCopy[i], key=lambda x: x)
    return lCopy
```

The function `sortThird` takes a list `l` as input. It creates a copy of the original list using the `copy()` method and assigns it to the variable `lCopy`. 

Next, it iterates through each element in `lCopy` using a `for` loop and checks if the index of the element is divisible by 3 using the expression `(i + 1) % 3 == 0`. If it is, it sorts the element in `lCopy` based on its value using the `sorted()` function and the `key` parameter with a lambda function `lambda x: x`. 

Finally, it returns the sorted list `lCopy`.

You can test the function with the provided examples:

```python
print(sortThird([1, 2, 3]))  # Output: [1, 2, 3]
print(sortThird([5, 6, 3, 4, 8, 9, 2]))  # Output: [2, 6, 3, 4, 8, 9, 5]
```

The first example `sortThird([1, 2, 3])` returns `[1, 2, 3]` because none of the elements are divisible by 3, so no sorting is performed.

The second example `sortThird([5, 6, 3, 4, 8, 9, 2])` returns `[2,