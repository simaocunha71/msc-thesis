Here's one way you could define such a function in Python:

```python
def max_Abs_Diff(lst):
    max_difference = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            max_difference = max(max_difference, abs(lst[i] - lst[j]))
    return max_difference
```

This function starts by initializing `max_difference` to zero. It then uses nested loops to compare every pair of distinct elements in the list. It calculates the absolute difference between each pair and updates `max_difference` if a larger difference is found. Finally, it returns the maximum difference found.

You can test this function with your example by running:

```python
print(max_Abs_Diff((2,1,5,3)))  # Outputs: 4
```

This will output `4`, which is the maximum absolute difference between any two elements in the list `(2,1,5,3)`.

```python
def max_Abs_Diff(lst):
    max_difference = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            max_difference = max(max_difference, abs(lst[i] - lst[j]))
    return max_difference
```
This function starts by initializing `max_difference` to zero. It then uses nested loops to compare every pair of distinct elements in the list. It calculates the absolute difference between each pair and updates `max_difference` if a larger difference is found. Finally, it returns the maximum difference found.

You can test this function with your example by running:
```python
print(max_Abs_Diff((2,1,5,3)))  # Outputs: 4
```
This will output `4`, which is the maximum absolute difference between any two elements in the list `(2,1,5,3)`.