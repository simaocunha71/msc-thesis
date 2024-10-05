  let result = 0;
  let current_row = 0;
  let current_col = 0;

  while (current_row < grid.length) {
    let current_cell = grid[current_row][current_col];
    if (current_cell == 1) {
      let current_row_max = 0;
      for (let i = current_row; i < grid.length; i++) {
        if (grid[i][current_col] == 1) {
          current_row_max += 1;
        } else {
          break;
        }
      }

      let current_col_max = 0;
      for (let j = current_col; j < grid[0].length; j++) {
        if (grid[current_row][j] == 1) {
          current_col_max += 1;
        } else {
          break;
        }
      }

      if (current_row_max <= capacity && current_col_max <= capacity) {
        current_row += current_row_max;
        current_col += current_col_max;
        result += 1;
      } else {
        current_row += capacity;
        current_col += capacity;
      }
    } else {
      current_row += 1;
    }
  }

  return result;
}



