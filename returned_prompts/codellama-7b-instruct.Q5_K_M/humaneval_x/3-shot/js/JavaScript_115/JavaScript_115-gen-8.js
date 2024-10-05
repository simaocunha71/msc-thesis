  let m = grid.length;
  let n = grid[0].length;
  let max_fill = 0;
  let bucket_fill = 0;
  let row = 0;
  let col = 0;

  while (row < m && col < n) {
    if (grid[row][col] == 0) {
      while (row < m && grid[row][col] == 0) row++;
      while (col < n && grid[row][col] == 0) col++;
    } else if (bucket_fill < capacity) {
      bucket_fill += grid[row][col];
      grid[row][col] = 0;
    } else {
      max_fill += 1;
      bucket_fill = 0;
    }
  }

  return max_fill;
}



