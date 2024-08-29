  const N = grid.length;
  const directions = [[-1, 0], [0, -1], [1, 0], [0, 1]];
  const visited = Array.from({length: N * N + 1}, () => false);
  const visited_pos = Array.from({length: N * N + 1}, () => []);

  const values = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      const index = i * N + j;
      values.push(grid[i][j]);
    }
  }

  const start = values[0];
  const end = start + k - 1;

  const queue = [];
  queue.push([start, 0]);
  visited[start] = true;
  while (queue.length > 0) {
    const [current_value, current_depth] = queue.shift();
    if (current_depth == k) {
      return visited_pos[current_value];
    }
    for (const direction of directions) {
      const new_row = current_value / N + direction[0];
      const new_col = (current_value % N) + direction[1];
      if (new_row >= 0 && new_row < N && new_col >= 0 && new_col < N) {
        const new_value = new_row * N + new_col;
        if (!visited[new_value]) {
          visited[new_value] = true;
          visited_pos[new_value] = visited_pos[current_value].concat([new_value]);
          queue.push([new_value, current_depth + 1]);
        }
      }
    }
  }

  return visited_pos[end];
}



