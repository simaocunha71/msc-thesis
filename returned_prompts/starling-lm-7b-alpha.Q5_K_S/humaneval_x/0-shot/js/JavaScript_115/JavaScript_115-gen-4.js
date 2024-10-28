/*
We can observe that the grid is a 2-dimensional array and represents a 2D matrix.
We can also observe that all rows have the same length.
In other words, the number of columns is the same for all rows.

We can start by computing the maximum number of buckets needed to empty a single row,
i.e. the maximum number of buckets needed to empty a single column in the worst case.
Let's call this value max_fill_one_row.

For example, if the grid is:
  [0, 0, 1, 1]
  [0, 1, 0, 0]
  [1, 1, 1, 1]

Then max_fill_one_row would be 4 because it takes 4 buckets to empty the column with the 1's.

Next, we can compute the maximum number of buckets needed to empty the whole grid,
i.e. the maximum number of buckets needed to empty all columns in the worst case.
Let's call this value max_fill_all_rows.

For example, if the grid is:
  [0, 0, 1, 1]
  [0, 1, 0, 0]
  [1, 1, 1, 1]

Then max_fill_all_rows would be 10 because it takes 10 buckets to empty all the columns with the 1's.

Finally, we can use the formula max_fill_all_rows = max_fill_one_row * number_of_columns to compute the maximum number of buckets needed to empty all the columns in the worst case.

For example, if the grid is:
  [0, 0, 1, 1]
  [0, 1, 0, 0]
  [1, 1, 1, 1]

Then max_fill_all_rows would be 4 * 4 = 16 because it takes 16 buckets to empty all the columns with the 1's.

So the final answer is max_fill_all_rows / capacity.

For example, if the grid is:
  [0, 