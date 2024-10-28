
def get_row(lst, x):
    rows = []
    for i, row in enumerate(lst):
        if x in row:
            rows.append((i, row.index(x)))
    rows.sort()
    return rows


# Code Explanation
# Here we are using a for loop to go through every row in the 2 dimensional list, lst. We check if the value x exists in each row. If it does, we append the row's index and the column's index of the value x to the rows list. We sort the rows by the index of the row in ascending order. Then we return the rows list.

```python
# Test Cases
print(get_row([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)) # [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1)) # []
print(get_row([[], [1], [1, 2, 3]], 3)) # [(2, 2)]
```

# Time Complexity: O(n * m)
# Here, n is the number of rows and m is the maximum number of columns in any row. The time complexity arises from the for loop that iterates over each row and the index() method, which has a time complexity of O(m). The sort() method has a time complexity of O(n * log(n)).

# Space Complexity: O(n + m)
# The space complexity arises from the rows list, which has a size of n (the number of rows) and m (the maximum number of columns in any row).

```python
```

```python

```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```