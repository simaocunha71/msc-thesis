/*
  Initialize a counter for the number of times you need to lower the buckets.
  Iterate through the grid and add the number of times you need to lower the buckets
  for each well.

  For each well, starting from the bottom-right, calculate the number of times
  you need to lower the buckets for each water unit.
  If the water units are less than or equal to the bucket capacity, add the number
  of times you need to lower the buckets for each water unit to the counter.
  Otherwise, add the number of times you need to lower the buckets for the bucket capacity.
  Then, for each row, starting from the bottom-left, if the water units are less than or
  equal to the bucket capacity, add the number of times you need to lower the buckets
  for each water unit to the counter. Otherwise, add the number of times you need to lower
  the buckets for the bucket capacity.
  If the water units are greater than the bucket capacity, the number of times you need
  to lower the buckets for the bucket capacity is equal to the number of times you need
  to lower the buckets for all the water units.

  Return the counter.

  Time Complexity: O(n * m)
  Space Complexity: O(1)

  where n is the number of rows, and m is the number of columns.
*/
  let counter = 0;

  for (let row = grid.length - 1; row >= 0; row--) {
    for (let col = grid[row].length - 1; col >= 0; col--) {
      if (grid[row][col] === 1) {
        if (row === grid.length - 1 && col === grid[row].length - 1) {
          counter += grid[row][col] % capacity === 0 ? 
            grid[row][col] / capacity : grid[row][col] / capacity + 1;
        } else if (row === grid.length - 1) {
          counter += grid[row][col] % capacity === 0 ? 
            grid[row][col] / capacity : grid[row][col] / capacity + 1;
        } else if (col