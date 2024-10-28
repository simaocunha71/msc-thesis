  let max_fill = 0;
  for (let i = 0; i < grid.length; i++) {
    let curr_fill = 0;
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        curr_fill += 1;
      } else {
        if (curr_fill >= capacity) {
          max_fill = Math.max(max_fill, curr_fill);
          curr_fill = 0;
        }
      }
    }
    max_fill = Math.max(max_fill, curr_fill);
  }
  return max_fill;
};
