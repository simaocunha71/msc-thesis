/*
  First, calculate the total amount of water in the grid by summing all the values
  in the grid. This will give us the upper bound on the number of times we need to
  lower the buckets. Then, for each row, calculate the amount of water that can
  be removed in a single pass. This will give us the lower bound on the number of
  times we need to lower the buckets. The actual number of times we need to lower the
  buckets will be between these two bounds.

  Let's denote the total amount of water as W, the amount of water that can be removed
  in a single pass as M, and the number of times we need to lower the buckets as N. We
  know that W = N * M, so we can rewrite the equation as N = W / M. Since N must be an
  integer, it must be the greatest integer less than or equal to W / M. We can calculate
  this using the Math.floor() function.

  To calculate M, we iterate over each row of the grid. For each row, we calculate the
  amount of water that can be removed in a single pass by summing all the values in the
  row. We then update the maximum amount of water that can be removed in a single pass
  by taking the maximum of the current maximum and the current row's sum. Finally, we
  calculate M as the sum of the maximum amount of water that can be removed in a single
  pass and the capacity of the bucket.

  To calculate W, we iterate over each row of the grid and calculate the amount of water
  in the row by summing all the values. We then update the total amount of water by adding
  the current row's sum to the total.

  Finally, we calculate and return the number of times we need to lower the buckets by
  taking the Math.floor() of W / M.
*/

  let totalWater = 0;
  for (let row of grid) {
    totalWater += row.reduce((acc, val) => acc + val, 0);
  }

  let maxRemovableWater = 0;
  for (let row of grid) {
    maxRemovableWater = Math.max(
     