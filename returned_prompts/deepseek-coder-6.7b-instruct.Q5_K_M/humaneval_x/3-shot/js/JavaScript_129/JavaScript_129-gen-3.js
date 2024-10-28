  const n = grid.length;
  const visited = Array(n).fill(0).map(() => Array(n).fill(false));
  const result = Array(k).fill(Infinity);
  const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];

  const dfs = (x, y, k, path) => {
    if (k === path.length) {
      for (let i = 0; i < path.length; i++) {
        if (path[i] < result[i]) {
          return true;
        } else if (path[i] > result[i]) {
          return false;
        }
      }
      return false;
    }

    for (let i = 0; i < directions.length; i++) {
      const nx = x + directions[i][0];
      const ny = y + directions[i][1];
      if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
        visited[nx][ny] = true;
        path.push(grid[nx][ny]);
        if (dfs(nx, ny, k, path)) {
          return true;
        }
        path.pop();
        visited[nx][ny] = false;
      }
    }

    return false;
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      visited[i][j] = true;
      if (dfs(i, j, k, [grid[i][j]])) {
        return result;
      }
      visited[i][j] = false;
    }
  }

  return result;
}



