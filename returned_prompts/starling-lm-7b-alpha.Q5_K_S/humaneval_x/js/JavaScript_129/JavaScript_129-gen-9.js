  const N = grid.length;
  const values = new Set(grid.flat());
  const index_map = new Map();
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      index_map.set(grid[i][j], [i, j]);
    }
  }

  const queue = new PriorityQueue({
    compare: (a, b) => index_map.get(a)[0] * N + index_map.get(a)[1] - (index_map.get(b)[0] * N + index_map.get(b)[1])
  });

  const seen = new Set();
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (values.has(i * N + j + 1)) {
        queue.push(i * N + j + 1);
      }
    }
  }

  while (queue.length > 0 && queue.length < k) {
    const next = queue.pop();
    if (!seen.has(next)) {
      queue.push(next);
      seen.add(next);
      const [i, j] = index_map.get(next);
      if (i > 0 && !seen.has(grid[i][j] - 1)) {
        queue.push(grid[i][j] - 1);
      }
      if (i + 1 < N && !seen.has(grid[i][j] + 1)) {
        queue.push(grid[i][j] + 1);
      }
      if (j > 0 && !seen.has(grid[i][j] - N)) {
        queue.push(grid[i][j] - N);
      }
      if (j + 1 < N && !seen.has(grid[i][j] + N)) {
        queue.push(grid[i][j] + N);
      }
    }
  }

  return queue.slice(0, k).