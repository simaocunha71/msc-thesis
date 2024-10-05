  var rows = grid.length;
  var columns = grid[0].length;
  var wells = new Array(rows);
  var wells_filled = new Array(rows);
  var wells_empty = new Array(rows);
  var current_bucket = 0;
  var total_filled = 0;

  for (let i = 0; i < rows; i++) {
    wells[i] = new Array(columns);
    wells_filled[i] = new Array(columns);
    wells_empty[i] = new Array(columns);
  }

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < columns; j++) {
      if (grid[i][j] == 1) {
        wells[i][j] = true;
        wells_filled[i][j] = false;
        wells_empty[i][j] = false;
      } else {
        wells[i][j] = false;
        wells_filled[i][j] = false;
        wells_empty[i][j] = true;
      }
    }
  }

  while (current_bucket < rows) {
    var current_well = current_bucket;
    var current_column = 0;
    while (current_column < columns) {
      if (wells[current_well][current_column] && !wells_empty[current_well][current_column]) {
        var current_row = current_well;
        var current_depth = 0;
        while (current_depth > -1 && current_row < rows) {
          if (wells[current_row][current_column]) {
            if (current_depth < capacity) {
              if (wells_filled[current_row][current_column]) {
                current_depth += 1;
              } else {
                wells_filled[current_row][current_column] = true;
                current_depth += 1;
              }
            } else {
              wells_empty[current_row][current_column] = true;
             