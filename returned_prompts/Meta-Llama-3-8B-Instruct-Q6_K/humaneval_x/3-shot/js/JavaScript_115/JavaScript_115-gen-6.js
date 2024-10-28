  let result = 0;
  let total = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      total += grid[i][j];
    }
  }

  while (total > 0) {
    result++;
    total -= capacity;
  }

  return result;
}