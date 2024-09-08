  const N = grid.length;
  const N2 = N * N;
  const neighbors = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
  ];

  const queue = [];
  const visited = new Set();
  const result = [];
  const directions = [];
  let cur_dist = k;
  let cur_num = 1;

  queue.push([0, 0]);
  while (queue.length > 0) {
    while (queue.length > 0 && cur_dist == 0) {
      const [x, y] = queue.pop();
      result.push(grid[x][y]);
      directions.push([x, y]);
      cur_dist -= 1;
    }
    while (queue.length > 0) {
      const [x, y] = queue.shift();
      if (visited.has(x * N + y)) {
        continue;
      }
      visited.add(x * N + y);
      for (const [dx, dy] of neighbors) {
        const x2 = x + dx;
        const y2 = y + dy;
        if (x2 >= 0 && x2 < N && y2 >= 0 && y2 < N && !visited.has(x2 * N + y2)) {
          if (cur_dist > 0) {
            cur_num = grid[x2][y2];
            queue.push([x2, y2]);
          } else {
            queue.unshift([x2, y2]);
          }
        }
      }
    }
    cur_dist -= 1;
    if (cur_dist >= 0) {
      cur_num += 1;
    }
  }

  return result;
};



