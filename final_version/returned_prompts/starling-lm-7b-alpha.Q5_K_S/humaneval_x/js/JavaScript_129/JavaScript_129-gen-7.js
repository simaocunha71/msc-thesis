  const N = grid.length;
  const L = Math.floor(k / N);
  const M = k % N;

  const start = (L == 0) ? N * N : grid[0][0];
  const end = (M == 0) ? N * N : grid[N - 1][M - 1];
  const path = [start];

  while (path.length < k) {
    if (L == 0) {
      path.push(grid[0][(M + 1) % N]);
      M = (M + 1) % N;
    } else {
      path.push(grid[N - 1][M]);
      L = L - 1;
      M = M - 1;
    }
  }

  return path.sort((a, b) => a - b);
}



