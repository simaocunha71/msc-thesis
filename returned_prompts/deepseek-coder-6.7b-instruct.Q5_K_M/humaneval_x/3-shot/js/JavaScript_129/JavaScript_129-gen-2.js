  const N = grid.length;
  const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];
  const visit = Array.from({length: N}, () => Array(N).fill(false));
  let result = Array(k).fill(Infinity);

  const dfs = (x, y, k, path) => {
    if (k === path.length) {
      result = [...path];
      return;
    }
    for (const [dx, dy] of directions) {
      const nx = x + dx, ny = y + dy;
      if (nx < 0 || nx >= N || ny < 0 || ny >= N || visit[nx][ny]) {
        continue;
      }
      if (path.length === 0 || (path.length < k && grid[nx][ny] > path[path.length - 1])) {
        visit[nx][ny] = true;
        dfs(nx, ny, k, [...path, grid[nx][ny]]);
        visit[nx][ny] = false;
      }
    }
  };

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      visit[i][j] = true;
      dfs(i, j, k, [grid[i][j]]);
      visit[i][j] = false;
    }
  }

  return result;
}



