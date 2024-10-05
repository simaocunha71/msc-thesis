  let rows = grid.length;
  let cols = grid[0].length;
  let totalWater = 0;
  let iterations = 0;

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] === 1) {
        totalWater += 1;
      }
    }
  }

  while (totalWater > 0) {
    iterations++;
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (grid[i][j] === 1) {
          totalWater--;
          grid[i][j] = 0;
        }
      }
    }
  }

  return iterations;
}

// This is a brute force approach. We are going through each cell, filling the bucket, and then lowering it until the bucket is empty.
// This approach is inefficient as it can be optimized by using a more clever approach such as using a priority queue to always fill the bucket with the most water. 