  let result = 0;
  for (let row = 0; row < grid.length; row++) {
    for (let col = 0; col < grid[row].length; col++) {
      if (grid[row][col] == 1) {
        result += capacity;
      }
    }
  }
  return result;
}