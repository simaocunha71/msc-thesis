  const n = grid.length;
  const m = grid[0].length;
  let count = 0;
  let bucket = Array(capacity).fill(1);
  let visited = Array(n).fill(Array(m).fill(0));

  while (true) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < m; j++) {
        if (visited[i][j] || grid[i][j] == 0) {
          continue;
        }
        if (bucket[0] == 0) {
          return count;
        }
        grid[i][j] = 0;
        visited[i][j] = 1;
        bucket[0] -= 1;
      }
    }
    count += 1;
    for (let i = n - 1; i >= 0; i--) {
      for (let j = m - 1; j >= 0; j--) {
        if (grid[i][j] == 0) {
          continue;
        }
        grid[i][j] = 0;
        bucket[0] += 1;
      }
    }
  }
}



