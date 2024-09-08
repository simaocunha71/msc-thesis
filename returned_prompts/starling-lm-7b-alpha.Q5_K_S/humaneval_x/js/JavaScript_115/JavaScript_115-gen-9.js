  let total_water = 0;
  for (let i = 0; i < grid.length; i++) {
    total_water += grid[i].reduce((total, x) => total + x);
  }

  let total_fill = 0;
  while (total_water > 0) {
    total_fill += 1;
    for (let i = 0; i < grid.length; i++) {
      while (grid[i].reduce((total, x) => total + x) >= capacity) {
        grid[i] = grid[i].map((x) => Math.max(0, x - capacity));
      }
    }
    total_water = grid.reduce((total, row) => total + row.reduce((total, x) => total + x), 0);
  }

  return total_fill;
}



