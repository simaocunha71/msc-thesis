  const rows = grid.length;
  const cols = grid[0].length;
  const values = [];

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      values.push(grid[r][c]);
    }
  }

  const min_path = [];
  const queue = [];
  const visited = [];

  for (let i = 0; i < k; i++) {
    queue.push(0);
    visited[0] = true;
  }

  while (queue.length > 0) {
    const current = queue.shift();
    const row = Math.floor(current / cols);
    const col = current % cols;
    if (col == cols - 1) {
      min_path.push(values[current]);
      current -= cols;
      queue.push(current);
    } else {
      const next = current + 1;
      if (!visited[next]) {
        queue.push(next);
        visited[next] = true;
      }
      const down = current + cols;
      if (!visited[down]) {
        queue.push(down);
        visited[down] = true;
      }
      const right = current + 1;
      if (!visited[right]) {
        queue.push(right);
        visited[right] = true;
      }
    }
  }

  return min_path;
}



