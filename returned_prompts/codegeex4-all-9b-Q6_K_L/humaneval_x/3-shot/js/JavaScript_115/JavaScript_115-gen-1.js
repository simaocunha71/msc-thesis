  var result = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] == 1) {
        result += 1;
      }
    }
  }

  return Math.floor(result / capacity);
}

