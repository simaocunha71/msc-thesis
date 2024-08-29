  const n = grid.length;
  const max = n * n;
  const visited = new Set();
  const q = new Set();
  const path = [];

  const enqueue = (x, y, p) => {
    if (x < 0 || y < 0 || x >= n || y >= n) return;
    if (visited.has(x * n + y)) return;
    visited.add(x * n + y);
    path.push(grid[x][y]);
    q.add(p.concat(grid[x][y]));
  };

  q.add([0, 0]);
  while (q.size) {
    const curr = q.pop();
    if (curr.length === k) return path;
    enqueue(curr[0], curr[1] + 1, curr);
    enqueue(curr[0] + 1, curr[1], curr);
    enqueue(curr[0], curr[1] - 1, curr);
    enqueue(curr[0] - 1, curr[1], curr);
  }
  return path;
}



