```
def max_of_nth(matrix, n):
    column = [row[n] for row in matrix]
    return max(column)
```

Explanation:

The function `max_of_nth` takes a matrix represented as a list of lists and an integer `n` as arguments. It uses a list comprehension to extract all the elements in the `n`-th column of the matrix. The `max()` function is then used to find the maximum value in the extracted column.

In the given example, `max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2)` is called, which corresponds to finding the maximum value in the second column of the matrix `[[5, 6, 7], [1, 3, 5], [8, 9, 19]]`. The result is `19`, as it is the maximum value in the second column.

The function returns the maximum value of the `n`-th column, which can be used for various purposes such as determining the maximum value in a specific column of a matrix.

Note: The function assumes that the matrix is non-empty and contains at least one column.

You can find more details about list comprehensions in Python in the [official Python documentation](https://docs.python.org/3/tutorial/lists.html#list-comprehensions).

Here is a step-by-step guide on how to use the function:

1. Define the matrix and the desired column index as input arguments for the `max_of_nth` function. For example, if you have a matrix called `matrix` and you want to find the maximum value in the second column, you would call the function like this: `max_of_nth(matrix, 1)`.

2. The function will return the maximum value in the specified column of the matrix. You can store the result in a variable or use it directly in your code. For example, you can print the result using `print(max_of_nth(matrix, 1))`.

3. The function will handle the extraction and comparison of the column values internally, so you don't need