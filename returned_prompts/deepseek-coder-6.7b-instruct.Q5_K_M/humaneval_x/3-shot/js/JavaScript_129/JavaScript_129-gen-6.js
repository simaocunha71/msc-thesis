  // The solution would require a dynamic programming approach, where we keep track of the minimum path
  // for each step and each cell.

  // We first convert the grid into a 1D array for easier handling.
  const flatGrid = grid.flat();

  // We then create an array to keep track of the minimum path for each cell.
  const minPath = new Array(flatGrid.length).fill(0);

  // We initialize the minimum path for the first cell to be the value of the first cell.
  minPath[0] = flatGrid[0];

  // We then iterate over each cell in the grid.
  for (let i = 0; i < flatGrid.length; i++) {
    // For each cell, we iterate over the k steps.
    for (let j = 1; j <= k; j++) {
      // For each step, we check all the possible cells that can be reached.
      // We then update the minimum path for the current cell.
      for (let m = 0; m < i; m++) {
        // We only consider cells that are adjacent to the current cell.
        if (Math.abs(flatGrid[i] - flatGrid[m]) <= j) {
          minPath[i] = Math.min(minPath[i], flatGrid[m] + minPath[m]);
        }
      }
    }
  }

  // Finally, we return the minimum path for the last cell.
  return minPath[flatGrid.length - 1];
}



