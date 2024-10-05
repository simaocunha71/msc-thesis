  const rows = grid.length;
  const cols = grid[0].length;

  const visited = new Set();
  const queue = [[[0, 0], 0]];

  const dirs = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
  ];

  while (queue.length > 0) {
    const [current, step] = queue.shift();
    if (visited.has(current)) continue;

    visited.add(current);

    if (step == k) {
      return current.map(v => grid[v[0]][v[1]]);
    }

    const [r, c] = current;
    for (const [dr, dc] of dirs) {
      const next_r = r + dr;
      const next_c = c + dc;

      if (0 <= next_r && next_r < rows && 0 <= next_c && next_c < cols) {
        const next = [next_r, next_c];
        if (!visited.has(next)) {
          queue.push([next, step + 1]);
        }
      }
    }
  }
}



