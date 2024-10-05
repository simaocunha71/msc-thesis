  let maxFill = 0;

  for (let i = 0; i < grid.length; i++) {
    let row = grid[i];
    let fill = 0;
    for (let j = 0; j < row.length; j++) {
      fill += row[j];
    }
    maxFill = Math.max(maxFill, fill);
  }

  return Math.ceil(maxFill / capacity);
}