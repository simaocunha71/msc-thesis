  let total = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      total += grid[i][j];
    }
  }
  
  return Math.ceil(total / capacity);
}



