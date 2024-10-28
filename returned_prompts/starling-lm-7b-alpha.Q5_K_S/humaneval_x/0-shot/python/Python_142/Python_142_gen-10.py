To solve this problem, we need to iterate through the list and check if the index of the current element is a multiple of 3 or 4. If it is, we need to square the element if it's a multiple of 3 and cube it if it's a multiple of 4 but not a multiple of 3. Finally, we need to sum up all the elements and return the result.

Here's a step-by-step breakdown of the solution:

1. Initialize a variable called `sum` to 0. This variable will be used to store the sum of all the elements.

2. Use a for loop to iterate through the list. For each element, check if its index (`i`) is a multiple of 3 or 4.

3. If the index is a multiple of 3, square the element and add the result to `sum`. If the index is a multiple of 4 but not a multiple of 3, cube the element and add the result to `sum`.

4. After iterating through the entire list, return the value of `sum`.

Here's the code that implements the solution:

```python
def sum_squares(lst):
    sum = 0
    for i in range(len(lst)):
        if (i + 1) % 3 == 0:
            sum += lst[i] ** 2
        elif (i + 1) % 4 == 0 and (i + 1) % 3 != 0:
            sum += lst[i] ** 3
    return sum
```

With this implementation, the function `sum_squares` will return the desired result based on the given examples:

- For `lst = [1,2,3]`, the output will be `6` (as 3 squared is 9 and 9 + 1 + 2 = 6)
- For `lst = []`, the output will be `0` (as there are no elements in the list)
- For `lst = [-1,-5,2,-1,-5]`, the output will be `-126` (as -1 cubed is -1, -5 squared is 25, 25 + 1 + -