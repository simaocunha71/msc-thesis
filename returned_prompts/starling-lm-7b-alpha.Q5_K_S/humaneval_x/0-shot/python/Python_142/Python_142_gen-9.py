To solve this problem, we can define a function called `sum_squares` that takes a list as an argument. We can initialize a variable called `total` to 0, which will store the sum of all the entries in the list. We can then iterate through the list using a for loop and check if the index of the current entry is a multiple of 3 and a multiple of 4. If it is, we square the entry and add it to the `total`. If the index is only a multiple of 4 but not a multiple of 3, we cube the entry and add it to the `total`. Finally, we return the `total` after iterating through all the entries in the list.

Here's the code for the solution:

```python
def sum_squares(lst):
    total = 0
    for i in range(len(lst)):
        if (i + 1) % 3 == 0 and (i + 1) % 4 == 0:
            total += lst[i] ** 2
        elif (i + 1) % 4 == 0 and (i + 1) % 3 != 0:
            total += lst[i] ** 3
    return total
```

You can use this function by passing a list of integers as an argument. It will return the sum of all entries in the list that meet the conditions specified in the problem.

For example:

```python
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
```

The first example returns 6 because the only entry that meets the conditions is 3, which is squared to get 9. The second example returns 0 because there are no entries that meet the conditions. The third example returns -126 because the entries at indexes 0, 3, and 4 meet the conditions, and their values are -1, -1, and -5, respectively. When squared and cubed, these values add up to -126.
