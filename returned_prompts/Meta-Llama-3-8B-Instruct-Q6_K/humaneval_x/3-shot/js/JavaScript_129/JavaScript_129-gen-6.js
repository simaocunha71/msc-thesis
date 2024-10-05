  const N = grid.length;
  const visited = new Array(N * N).fill(false);
  const res = [];
  const dfs = (x, y, path) => {
    if (path.length === k) {
      res.push(path);
      return;
    }
    for (let dx = -1; dx <= 1; dx++) {
      for (let dy = -1; dy <= 1; dy++) {
        if (dx === 0 && dy === 0) continue;
        let nx = x + dx;
        let ny = y + dy;
        if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx * N + ny]) {
          visited[nx * N + ny] = true;
          dfs(nx, ny, [...path, grid[nx][ny]]);
          visited[nx * N + ny] = false;
        }
      }
    }
  };
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      visited[i * N + j] = true;
      dfs(i, j, [grid[i][j]]);
      visited[i * N + j] = false;
    }
  }
  res.sort((a, b) => a.join('') < b.join('') ? -1 : 1);
  return res[0];
}