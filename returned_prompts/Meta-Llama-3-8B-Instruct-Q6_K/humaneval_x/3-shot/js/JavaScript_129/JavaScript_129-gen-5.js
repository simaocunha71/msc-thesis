  let N = grid.length;
  let visited = Array.from({ length: N }, () => Array(N).fill(false));
  let res = [];
  let minRes = Array(k + 1).fill(Infinity);
  let minResPath = [];

  let dfs = (x, y, path) => {
    if (path.length > k) return;
    if (path.length === k) {
      if (path < minRes) {
        minRes = path;
        minResPath = path;
      }
      return;
    }
    for (let dx of [-1, 0, 1]) {
      for (let dy of [-1, 0, 1]) {
        let nx = x + dx;
        let ny = y + dy;
        if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
          visited[nx][ny] = true;
          dfs(nx, ny, path.concat(grid[nx][ny]));
          visited[nx][ny] = false;
        }
      }
    }
  };

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      visited[i][j] = true;
      dfs(i, j, [grid[i][j]]);
      visited[i][j] = false;
    }
  }

  return minResPath;
}  // This is a brute force solution using DFS. It can be optimized by using a priority queue to keep track of the minimum path length and the corresponding path.
}  // This is a brute force solution using DFS. It can be optimized by using a priority queue to keep track of the minimum path length and the corresponding path.