  var max_fills = 0;
  var current_fills = 0;

  for (var row_index = 0; row_index < grid.length; row_index++) {
    var current_row = grid[row_index];
    var row_max_fill = 0;

    for (var col_index = 0; col_index < current_row.length; col_index++) {
      if (current_row[col_index] == 1) {
        row_max_fill += 1;
      }
    }

    if (row_max_fill > capacity) {
      var row_fills = 0;

      for (var col_index = 0; col_index < current_row.length; col_index++) {
        if (current_row[col_index] == 1) {
          row_fills += 1;
          current_fills += 1;
        }

        if (row_fills > capacity) {
          max_fills = Math.max(max_fills, current_fills);
          current_fills = 0;
        }
      }
    } else {
      max_fills = Math.max(max_fills, current_fills);
      current_fills = 0;
    }
  }

  return max_fills;
}



