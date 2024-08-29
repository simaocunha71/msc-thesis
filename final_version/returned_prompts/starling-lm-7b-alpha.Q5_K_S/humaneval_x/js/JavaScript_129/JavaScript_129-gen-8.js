  const grid_length = grid.length;
  const grid_width = grid[0].length;

  let visited = new Set();
  let queue = [];

  for (let i = 0; i < grid_length; i++) {
    for (let j = 0; j < grid_width; j++) {
      queue.push([i, j]);
      visited.add(grid[i][j]);
    }
  }

  while (queue.length != 0 && visited.size < grid_length * grid_width) {
    const current_cell = queue.shift();
    const i = current_cell[0];
    const j = current_cell[1];
    if (i < grid_length - 1 && visited.add(grid[i + 1][j])) {
      queue.push([i + 1, j]);
    }
    if (i > 0 && visited.add(grid[i - 1][j])) {
      queue.push([i - 1, j]);
    }
    if (j < grid_width - 1 && visited.add(grid[i][j + 1])) {
      queue.push([i, j + 1]);
    }
    if (j > 0 && visited.add(grid[i][j - 1])) {
      queue.push([i, j - 1]);
    }
  }

  const path_length = k;
  const path_values = [];

  while (path_length != 0) {
    const next_cell = queue[path_length - 1];
    path_values.push(grid[next_cell[0]][next_cell[1]]);
    path_length--;
  }

  return path_values;
}



