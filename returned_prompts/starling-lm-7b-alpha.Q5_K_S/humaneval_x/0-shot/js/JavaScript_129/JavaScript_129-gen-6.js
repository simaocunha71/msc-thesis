  const set = new Set();

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      set.add(grid[i][j]);
    }
  }

  const queue = [];

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (i > 0 && grid[i][j] > grid[i - 1][j]) {
        queue.push(grid[i][j]);
      }
      if (j > 0 && grid[i][j] > grid[i][j - 1]) {
        queue.push(grid[i][j]);
      }
    }
  }

  if (queue.length < k) {
    return queue;
  }

  const res = [];
  let tempQueue = queue.slice(0, k);

  while (tempQueue.length) {
    const top = tempQueue.shift();
    if (!set.has(top)) {
      return res;
    }
    res.push(top);
    while (true) {
      if (top > 0 && grid[top - 1][0] === top && !set.has(grid[top - 1][0])) {
        tempQueue.push(grid[top - 1][0]);
      } else if (top > 0 && grid[top - 1][1] === top && !set.has(grid[top - 1][1])) {
        tempQueue.push(grid[top - 1][1]);
      } else if (top > 0 && grid[top - 1][grid[top - 1].length - 1] === top && !set.has(grid[top - 1][grid[top - 1].length - 1])) {
        tempQueue.push(grid[top - 1][grid[top - 1].length - 1]);
      } else if (top < grid.length - 1 && grid[top + 1][0]