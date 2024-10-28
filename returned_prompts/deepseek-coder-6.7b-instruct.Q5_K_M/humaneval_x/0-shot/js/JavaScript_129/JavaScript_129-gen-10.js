  // Initialization of variables
  const N = grid.length;
  const visited = Array.from({length: N}, () => Array(N).fill(false));
  const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];
  let minPath = Array(k).fill(Infinity);
  let result = Array(k).fill(Infinity);
  
  // Recursive function for DFS
  const dfs = (x, y, path) => {
    if (path.length === k) {
      if (compare(path, minPath) < 0) {
        minPath = [...path];
      }
      return;
    }
    for (let i = 0; i < 4; i++) {
      const nx = x + directions[i][0];
      const ny = y + directions[i][1];
      if (nx < 0 || nx >= N || ny < 0 || ny >= N || visited[nx][ny]) continue;
      visited[nx][ny] = true;
      dfs(nx, ny, [...path, grid[nx][ny]]);
      visited[nx][ny] = false;
    }
  }

  // Comparator for lexicographically comparison
  const compare = (a, b) => {
    for (let i = 0; i < k; i++) {
      if (a[i] !== b[i]) return a[i] - b[i];
    }
    return 0;
  }

  // Start from every cell
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      visited[i][j] = true;
      dfs(i, j, [grid[i][j]]);
      visited[i][j] = false;
    }
  }

  return minPath;
};


console.log(minPath([[1,2,3], [4,5,6], [7,8,9]], 3));