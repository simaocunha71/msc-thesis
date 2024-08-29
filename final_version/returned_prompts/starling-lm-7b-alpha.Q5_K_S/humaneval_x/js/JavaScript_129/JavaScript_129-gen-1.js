  let n = grid.length;
  let result = [];
  let min_val = k + 1;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] < min_val) {
        min_val = grid[i][j];
        result = [grid[i][j]];
      } else if (grid[i][j] == min_val) {
        result.push(grid[i][j]);
      }
    }
  }

  while (result.length < k) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        for (let d = 0; d < 4; d++) {
          let new_i = i + dx[d];
          let new_j = j + dy[d];
          if (new_i < 0 || new_i >= n || new_j < 0 || new_j >= n) {
            continue;
          }
          if (grid[new_i][new_j] < min_val) {
            min_val = grid[new_i][new_j];
            result = [grid[new_i][new_j]];
          } else if (grid[new_i][new_j] == min_val) {
            result.push(grid[new_i][new_j]);
          }
        }
      }
    }
  }
  return result;
}


dx = [0, 1, 0, -1];
dy = [1, 0, -1, 0];



