  let rows = grid.length;
  let cols = grid[0].length;

  let sum = 0;
  for (let i = 0; i < rows; i++) {
    sum += grid[i].reduce((a, b) => a + b);
  }

  let total_buckets = Math.ceil(sum / capacity);
  let current_bucket = 0;
  let current_row = 0;
  while (current_bucket < total_buckets) {
    if (current_row < rows) {
      for (let i = 0; i < cols; i++) {
        if (grid[current_row][i] > 0) {
          grid[current_row][i]--;
          current_bucket++;
          if (current_bucket == total_buckets) {
            return current_bucket;
          }
        }
      }
    }
    current_row++;
  }

  return total_buckets;
}



