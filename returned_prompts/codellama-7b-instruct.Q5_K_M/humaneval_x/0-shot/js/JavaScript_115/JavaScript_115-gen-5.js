/*
  Approach:

  * We can use a BFS to fill each well, starting from the top row.
    If we encounter a 1, we can fill it. If we encounter a 0, we cannot fill it.
    If we reach the end of a row and we have not filled all the cells in that row,
    we can fill the remaining cells with 0s.
    We can then start filling the next row, and so on.
  * We can keep a count of how many times we need to lower the bucket.
    If we encounter a 1, we need to lower the bucket once. If we encounter a 0,
    we need to lower the bucket once for each cell in that row that we did not fill.

  Time complexity: O(n)
    - n is the number of rows in the grid

  Space complexity: O(1)
    - We only need to keep track of the current row, the current column,
      and the total number of times we need to lower the bucket.
*/

  let rows = grid.length;
  let cols = grid[0].length;
  let total = 0;

  for (let row = 0; row < rows; row++) {
    let currentRow = row;
    let currentCol = 0;
    let currentFillCount = 0;

    while (currentCol < cols) {
      if (grid[currentRow][currentCol] === 1) {
        currentFillCount++;
      }

      if (currentCol === cols - 1) {
        total += currentFillCount;
      }

      if (currentRow === rows - 1) {
        total += cols - currentCol - 1;
      }

      currentRow++;
      currentCol++;
    }

    total += rows - currentRow;
  }

  return total;
};
