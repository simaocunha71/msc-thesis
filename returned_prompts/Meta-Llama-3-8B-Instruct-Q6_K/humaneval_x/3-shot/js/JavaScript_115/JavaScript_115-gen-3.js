  let count = 0;
  for (let i = 0; i < grid.length; i++) {
    let water = 0;
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        water += 1;
      }
    }
    while (water > 0) {
      water -= capacity;
      count += 1;
    }
  }
  return count;
}