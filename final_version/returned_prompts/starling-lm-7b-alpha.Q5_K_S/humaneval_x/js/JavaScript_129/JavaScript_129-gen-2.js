  const N = grid.length;
  const neighbors = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
  ];

  let queue = [];
  let visited = Array(N).fill(false);
  let path = [];

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      queue.push([i, j, grid[i][j]]);
      visited[i] = true;
    }
  }

  queue.sort((a, b) => {
    if (a[2] < b[2]) return -1;
    if (a[2] > b[2]) return 1;
    return 0;
  });

  while (queue.length && path.length < k) {
    const [i, j, value] = queue.shift();
    visited[i] = false;

    for (const [dx, dy] of neighbors) {
      const [n_i, n_j] = [i + dx, j + dy];
      const n_value = grid[n_i][n_j];
      if (n_i >= 0 && n_i < N && n_j >= 0 && n_j < N && visited[n_i]) {
        path.push(n_value);
        queue.push([n_i, n_j, n_value]);
      }
    }
  }

  return path;
};



