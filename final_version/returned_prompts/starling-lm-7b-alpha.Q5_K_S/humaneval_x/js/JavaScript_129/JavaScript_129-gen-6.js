  let m = grid.length;
  let visited = new Set();
  let queue = [];
  queue.push([0, 0, 0]);
  let result = [];
  while (queue.length > 0) {
    let [r, c, t] = queue.shift();
    if (t == k) {
      result.push(grid[r][c]);
      continue;
    }
    if (!visited.has(r * m + c)) {
      visited.add(r * m + c);
      queue.push([r, c, t + 1]);
      if (r != 0) {
        queue.push([r - 1, c, t + 1]);
      }
      if (c != m - 1) {
        queue.push([r, c + 1, t + 1]);
      }
    }
  }
  return result;
}



