# Here is a solution to the problem above
def sum_squares(lst):
    lst = [int(i) for i in lst]
    return sum([i ** 2 for i in lst])

# Here are some tests you can use to check your implementation
print(sum_squares([1, 2, 3]))  # Expected output: 14
print(sum_squares([1, 4, 9]))  # Expected output: 98
print(sum_squares([1, 3, 5, 7]))  # Expected output: 84
print(sum_squares([1.4, 4.2, 0]))  # Expected output: 29
print(sum_squares([-2.4, 1, 1]))  # Expected output: 6



# Here is some explanation for the solution above
# The solution first converts the list to a list of integers
# Then it squares each element and sums the results
# This gives us the sum of the squares of all the elements in the list

```

Answer: Here is a solution to the problem above

```
def sum_squares(lst):
    lst = [int(i) for i in lst]
    return sum([i ** 2 for i in lst])
```

Here are some tests you can use to check your implementation

```python
print(sum_squares([1, 2, 3]))  # Expected output: 14
print(sum_squares([1, 4, 9]))  # Expected output: 98
print(sum_squares([1, 3, 5, 7]))  # Expected output: 84
print(sum_squares([1.4, 4.2, 0]))  # Expected output: 29
print(sum_squares([-2.4, 1, 1]))  # Expected output: 6
```

Here is some explanation for the solution above
The solution first converts the list to a list of integers
