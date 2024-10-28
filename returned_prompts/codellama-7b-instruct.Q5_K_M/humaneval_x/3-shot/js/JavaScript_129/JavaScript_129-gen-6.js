  let visited = new Array(grid.length).fill(false);
  let queue = [];
  let path = [];
  let i = 0;

  while (k > 0) {
    if (i >= grid.length) {
      i = 0;
    }
    if (!visited[i]) {
      queue.push(i);
      visited[i] = true;
    }

    i = queue[0];
    for (let j = 0; j < grid.length; j++) {
      if (grid[i][j] != 0 && !visited[j]) {
        queue.push(j);
        visited[j] = true;
      }
    }
    path.push(grid[i][i]);
    k--;
  }
  return path;
}



