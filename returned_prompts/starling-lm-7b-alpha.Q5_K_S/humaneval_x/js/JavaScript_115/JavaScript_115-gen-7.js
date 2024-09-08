  let result = 0;
  let count = 0;
  let used = false;
  let grid_size = grid[0].length;

  while (count < grid.length) {
    used = false;
    for (let i = 0; i < grid_size; i++) {
      if (grid[count][i] == 1) {
        grid[count][i] = 0;
        count++;
        result++;
        used = true;
        break;
      }
    }
    if (!used) {
      for (let i = grid_size - 1; i >= 0; i--) {
        if (grid[count][i] == 1) {
          grid[count][i] = 0;
          count++;
          result++;
          used = true;
          break;
        }
      }
    }
  }

  return result;
}



