  const rows = grid.length;
  const cols = grid[0].length;
  const N = rows * cols;

  const visited = new Array(N).fill(false);
  const queue = [[0, 0, 0]];
  const result = [];

  while (queue.length > 0) {
    const [row, col, length] = queue.shift();

    const new_length = length + 1;
    if (new_length > k) {
      continue;
    }

    for (let [dr, dc] of [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ]) {
      const new_row = row + dr;
      const new_col = col + dc;
      if (new_row < 0 || new_row >= rows || new_col < 0 || new_col >= cols) {
        continue;
      }

      const new_index = new_row * cols + new_col;
      if (visited[new_index]) {
        continue;
      }

      queue.push([new_row, new_col, new_length]);
      visited[new_index] = true;
    }

    result.push(grid[row][col]);
  }

  return result;
}



