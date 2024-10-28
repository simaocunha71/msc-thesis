  const m = grid.length;
  const n = grid[0].length;

  let min_path = [];
  let min_path_value = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      let path = [];
      let current_cell = { i, j };
      let current_path_value = 0;
      for (let l = 1; l <= k; l++) {
        let neighbor_cells = getNeighborCells(current_cell, m, n);
        for (let neighbor_cell of neighbor_cells) {
          if (neighbor_cell.i == m - 1 && neighbor_cell.j == n - 1) {
            current_path_value += grid[neighbor_cell.i][neighbor_cell.j];
            min_path_value = Math.min(min_path_value, current_path_value);
            min_path = [...min_path, ...path, grid[neighbor_cell.i][neighbor_cell.j]];
            break;
          }
          if (neighbor_cell.i == m - 1) {
            current_path_value += grid[neighbor_cell.i][neighbor_cell.j];
          } else if (neighbor_cell.j == n - 1) {
            current_path_value += grid[neighbor_cell.i][neighbor_cell.j];
          } else {
            current_path_value += grid[neighbor_cell.i][neighbor_cell.j];
          }
        }
      }
    }
  }

  return min_path;
}



