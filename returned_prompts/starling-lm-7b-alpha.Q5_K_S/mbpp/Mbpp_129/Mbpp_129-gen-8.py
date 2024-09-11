Here's a Python function that can be used to check whether a matrix is a magic square:

```python
def magic_square_test(matrix):
    # Flatten the matrix and sort the result
    flat_list = [row[col] for row in matrix for col in range(len(matrix))]
    flat_list.sort()

    # If the sorted result is not equal to the original, then it's not a magic square
    return flat_list == list(map(sum, zip(*matrix)))
```

You can use the provided test case to check if the function is working correctly:

```python
matrix = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
print(magic_square_test(matrix))  # Should print True
```

This function works by first flattening the matrix into a single list, then sorting that list. It then checks if the sorted result is equal to the sum of each row or column in the original matrix. If they are equal, then the matrix is a magic square.

This approach is based on the properties of a magic square, which include:

1. The sum of each row, column, and diagonal is equal.
2. Each number from 1 to N (where N is the size of the square) appears exactly once in each row, column, and diagonal.

The function tests the first property to determine if the matrix is a magic square.

The time complexity of this function is O(N^2) because it needs to iterate through the entire matrix to flatten it. The space complexity is also O(N^2) because it creates a new list to store the flattened matrix.
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
