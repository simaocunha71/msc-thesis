  let result = 0;
  for (let i = 0; i < grid.length; i++) {
    let current_water = 0;
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] == 1) {
        current_water += 1;
      }
    }

    if (current_water > capacity) {
      result += Math.ceil(current_water / capacity);
    }
  }

  return result;
}



