  let result = 0;
  let current_row = 0;
  let current_col = 0;
  let current_bucket = 0;
  let current_row_max = 0;
  let current_col_max = 0;

  while (current_row < grid.length) {
    current_row_max = 0;
    for (let i = 0; i < grid[current_row].length; i++) {
      if (grid[current_row][i] > 0) {
        current_row_max += grid[current_row][i];
        current_col = i;
      }
    }
    current_col_max = 0;
    for (let i = 0; i < grid[current_row].length; i++) {
      if (grid[i][current_col] > 0) {
        current_col_max += grid[i][current_col];
      }
    }

    if (current_row_max <= capacity && current_col_max <= capacity) {
      current_row++;
      continue;
    }

    if (current_row_max <= capacity) {
      current_col++;
      continue;
    }

    if (current_col_max <= capacity) {
      current_row++;
      continue;
    }

    let current_row_bucket = Math.floor(current_row_max / capacity);
    let current_col_bucket = Math.floor(current_col_max / capacity);
    let current_row_remainder = current_row_max % capacity;
    let current_col_remainder = current_col_max % capacity;

    if (current_row_remainder > 0) {
      current_row_bucket++;
    }
    if (current_col_remainder > 0) {
      current_col_bucket++;
    }

    if (current_row_bucket > current_col_bucket) {
      current_col++;
    } else {
      current_row++;
    }

    result++;
  }

  return result;
}



