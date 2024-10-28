  const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
  const N = grid.length;
  const result = [];
  
  const dfs = (x, y, k, path) => {
    if (k === 0) {
      result.push(path.slice());
      return;
    }
    for (let i = 0; i < directions.length; i++) {
      const nx = x + directions[i][0];
      const ny = y + directions[i][1];
      if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
        path.push(grid[nx][ny]);
        dfs(nx, ny, k - 1, path);
        path.pop();
      }
    }
  };
  
  let minPath = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      dfs(i, j, k - 1, [grid[i][j]]);
    }
  }
  
  result.sort((a, b) => {
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) return a[i] - b[i];
    }
    return 0;
  });
  
  return result[0];
}



