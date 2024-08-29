  let total_water = 0;
  let result = 0;
  while (total_water < grid.length * grid[0].length) {
    for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[i].length; j++) {
        if (grid[i][j] == 1) {
          grid[i][j] = 0;
          total_water += 1;
          if (total_water % capacity == 0) {
            result += 1;
          }
        }
      }
    }
  }
  return result;
}



