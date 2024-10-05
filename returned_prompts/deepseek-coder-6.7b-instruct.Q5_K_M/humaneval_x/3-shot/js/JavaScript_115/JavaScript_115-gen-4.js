  let count = 0;
  for  (let i = 0; i < grid.length; i++) {
    for  (let j = 0; j < grid[i].length; j++) {
      if  (grid[i][j] == 1) {
        count += Math.ceil(grid[i].reduce((a, b) => a + b, 0) / capacity);
      }
    }
  }
  return count;
}



