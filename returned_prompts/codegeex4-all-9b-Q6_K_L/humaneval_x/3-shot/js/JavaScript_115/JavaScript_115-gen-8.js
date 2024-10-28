  let count = 0;
  let rows = grid.length;
  let cols = grid[0].length;

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] == 1) {
        count += Math.ceil(grid[i][j] / capacity);
      }
    }
  }

  return count;
}



