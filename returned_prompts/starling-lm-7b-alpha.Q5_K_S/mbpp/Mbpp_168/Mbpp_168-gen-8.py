```python
def frequency(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count
```

Explanation:
The function `frequency` takes in two parameters: `lst` and `x`. It initializes a variable `count` to 0. It then iterates over each element `i` in the given `lst`. If `i` is equal to `x`, the `count` variable is incremented by 1. After iterating through all the elements, the function returns the final value of `count`, which represents the number of occurrences of `x` in the list.

In the provided test case, `frequency([1,2,3], 4)` is called, which checks if the function correctly returns 0 when the number 4 is not present in the list `[1,2,3]`.

This solution uses a simple approach of counting the occurrences of a number in a list by iterating through each element and incrementing a counter variable when a match is found.

You can use this function to count the occurrences of any number in a given list. Just pass the list and the number you want to count as arguments to the `frequency` function, and it will return the count of occurrences.

Note that this solution assumes that the input list contains only integer elements. If you need to count occurrences in a list of non-integer elements, you would need to modify the function accordingly.

I hope this helps! Let me know if you have any more questions.
```

```python
def frequency(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count
```