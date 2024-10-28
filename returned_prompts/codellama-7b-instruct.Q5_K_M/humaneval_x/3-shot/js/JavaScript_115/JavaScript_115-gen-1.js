  const rows = grid.length;
  const cols = grid[0].length;
  const visited = new Array(rows).fill(false).map(i => new Array(cols).fill(false));
  var max_fill = 0;

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (grid[row][col] == 1 && !visited[row][col]) {
        visited[row][col] = true;
        let current_row = row;
        let current_col = col;
        let current_fill = 0;
        while (current_row >= 0 && current_col >= 0 && current_row < rows && current_col < cols && grid[current_row][current_col] == 1) {
          if (current_fill < capacity) {
            visited[current_row][current_col] = true;
            current_fill += 1;
          } else {
            break;
          }
          current_row -= 1;
          current_col -= 1;
        }
        max_fill = Math.max(max_fill, current_fill);
      }
    }
  }

  return max_fill;
}



