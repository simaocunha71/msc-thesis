  const n = grid.length;
  let res = [];
  let min_res = [];
  let max_res = [];
  let current_res = [];
  let current_min_res = [];
  let current_max_res = [];

  let i = 0;
  while (i < k) {
    let j = 0;
    while (j < n) {
      current_res.push(grid[i % n][j % n]);
      if (current_res.length == k) {
        if (current_res.join('').localeCompare(res.join('')) < 0) {
          res = current_res;
          min_res = current_min_res;
          max_res = current_max_res;
        } else if (current_res.join('').localeCompare(res.join('')) == 0) {
          if (min_res.length == 0) {
            min_res = current_min_res;
          }
          if (max_res.length == 0) {
            max_res = current_max_res;
          }
        }
        current_res = [];
        current_min_res = [];
        current_max_res = [];
      }
      if (j < n - 1) {
        current_min_res.push(grid[i % n][j % n + 1]);
        current_max_res.push(grid[i % n][j % n + 1]);
      }
      if (i < n - 1) {
        current_min_res.push(grid[i % n + 1][j % n]);
        current_max_res.push(grid[i % n + 1][j % n]);
      }
      if (i < n - 1 && j < n - 1) {
        current_min_res.push(grid[i % n + 1][j % n + 1]);
        current_max_res.push(grid[i % n + 1][j % n + 1]);
      }
      j += 1;
    }
    i += 1;
  }
