  var result = 0;
  var curr_row = 0;
  var curr_col = 0;
  var curr_capacity = capacity;
  var curr_well = 0;
  var curr_well_capacity = 0;

  while (curr_well < grid.length) {
    // Check if current well is empty. If not, check if current well is full.
    if (grid[curr_well][curr_col] == 1) {
      if (curr_capacity == 0) {
        // Current well is empty, but current row is full. Move to next well.
        curr_well++;
        curr_capacity = capacity;
        curr_row = 0;
        curr_col = 0;
      } else {
        // Current well is not empty, but current well is not full.
        // Fill current well.
        curr_well_capacity = grid[curr_well][curr_col];
        curr_well_capacity = Math.min(curr_well_capacity, curr_capacity);
        curr_capacity -= curr_well_capacity;
        grid[curr_well][curr_col] -= curr_well_capacity;
      }
    } else {
      // Current well is empty, and current row is not full.
      // Move to next row.
      curr_row++;
      curr_capacity = capacity;
      if (curr_row == grid[curr_well].length) {
        // Current well is empty, and current row is full. Move to next well.
        curr_well++;
        curr_capacity = capacity;
        curr_row = 0;
        curr_col = 0;
      }
    }
    result++;
  }

  return result;
}



