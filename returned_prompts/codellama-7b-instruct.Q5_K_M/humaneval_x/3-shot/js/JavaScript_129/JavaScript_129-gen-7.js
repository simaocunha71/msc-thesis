  const rows = grid.length;
  const cols = grid[0].length;

  const dirs = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
  ];

  const visited = new Set();
  const queue = [[[0, 0, 0], 0]];

  while (queue.length) {
    const [x, y, depth] = queue.shift();

    if (visited.has(x + ',' + y)) {
      continue;
    }

    visited.add(x + ',' + y);

    if (depth === k) {
      return grid[x][y];
    }

    for (const [dx, dy] of dirs) {
      const nx = x + dx;
      const ny = y + dy;

      if (nx < 0 || nx >= rows || ny < 0 || ny >= cols) {
        continue;
      }

      queue.push([nx, ny, depth + 1]);
    }
  }

  return [];
}



