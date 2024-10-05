To solve this problem, I would use a nested loop to iterate through the array of numbers and check if there are three numbers that sum up to zero. Here's a step-by-step explanation of the solution:

1. Define a function called `triplesSumToZero` that takes an array `l` as input.
2. Initialize a variable `found` to `false` to keep track of whether three numbers that sum to zero have been found.
3. Use a nested loop to iterate through the array `l`. The outer loop iterates from the first element to the third-to-last element, and the inner loop iterates from the element next to the outer loop's current element to the last element.
4. Inside the nested loop, check if the sum of the current three elements is equal to zero. If it is, set `found` to `true` and break out of the loop.
5. After the nested loop finishes, return the value of `found`.
6. Finally, define some test cases and use the `print` function to display the result of the `triplesSumToZero` function for each test case.

Here's the code for the solution:

```python
def triplesSumToZero(l):
    found = False
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] + l[j + 1] == 0:
                found = True
                break
    return found
```

```python
print(triplesSumToZero([1, 3, 5, 0]))  # False
print(triplesSumToZero([1, 3, -2, 1]))  # True
print(triplesSumToZero([1, 2, 3, 7]))  # False
print(triplesSumToZero([2, 4, -5, 3, 9, 7]))  # True
print(triplesSumToZero([1]))  # False
```

By following this approach, the `triplesSumToZero` function will return `True` if there are three distinct elements in the input array `l` that sum to zero, and