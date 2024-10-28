
Explanation:
The function `get_row` takes a 2D list `lst` and an integer `x` as input. It iterates over each row in the list, and for each row, it checks if `x` is present in that row. If `x` is present, it finds the indices of `x` in the row and adds them to the result list. The indices are added in reverse order to ensure that the columns are sorted in descending order within each row. Finally, the result list is sorted by row indices in ascending order.

Here's a step-by-step breakdown of the function:

1. Initialize an empty list `result` to store the coordinates.
2. Iterate over each row `row` in the list `lst` using `enumerate`, which returns both the index `i` and the value `row`.
3. Check if `x` is present in the current row using the `in` operator.
4. If `x` is present, find the indices of `x` in the row using a list comprehension.
5. Add the indices to the `result` list as tuples, where each tuple contains the row index `i` and the column index.
6. Sort the `result` list by row indices in ascending order and then by column indices in descending order using the `sorted` function.
7. Return the sorted `result` list.

The examples provided in the problem statement demonstrate the expected output for different inputs. For instance, `get_row([[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]], 1)` should return `[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]`, which is the correct output. The function should work correctly for empty lists, lists with single elements, and lists with multiple elements.