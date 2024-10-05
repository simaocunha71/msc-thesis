  let result = 0;
  for (let i = 0; i < grid.length; i++) {
    let row = grid[i];
    let total = 0;
    for (let j = 0; j < row.length; j++) {
      if (row[j] == 1) {
        total += 1;
      }
    }
    result += Math.ceil(total / capacity);
  }
  return result;
}