/*
  Brute force approach would be to find the max height of the grid, and then
  iterate over each row and column to find the maximum water that can be 
  filled.
  Time complexity would be O(n^2).
  */
  const maxHeight = grid.length;
  let totalFilledWater = 0;

  for (let i = 0; i < maxHeight; i++) {
      let maxWater = 0;
      for (let j = 0; j < grid[i].length; j++) {
          if (grid[i][j] === 1) {
              maxWater = Math.max(maxWater, grid[i][j]);
          }
      }
      totalFilledWater += maxWater;
  }

  return totalFilledWater;

B:
/*
  A more efficient approach is to use a single pass over the grid, by keeping track
  of the maximum height of the water that can be filled in each cell.
  We can do this by using a 2D array to store the maximum height of water in each cell.
  The time complexity is O(n^2).
  */
  const maxHeight = grid.length;
  const maxWater = new Array(maxHeight).fill(0).map(x => new Array(maxHeight).fill(0));
  let totalFilledWater = 0;

  for (let i = 0; i < maxHeight; i++) {
      for (let j = 0; j < grid[i].length; j++) {
          if (grid[i][j] === 1) {
              maxWater[i][j] = 1;
          } else {
              if (i - 1 >= 0) {
                  maxWater[i][j] = Math.max(maxWater[i - 1][j], maxWater[i][j]);
              }
              if (j - 1 >= 0) {
                  maxWater[i][j] = Math.max(maxWater[i][j - 1], maxWater[i][j]);
              }
          }
      }
 