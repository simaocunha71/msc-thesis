  let N = grid.length;
  let result = new Array(k);
  let visited = new Array(N * N).fill(false);
  let queue = [];
  let directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  let sum = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visited[i * N + j]) {
        visited[i * N + j] = true;
        queue.push([i, j, [grid[i][j]], 1]);
      }
    }
  }

  while (queue.length > 0) {
    let [x, y, path, len] = queue.shift();
    if (len == k) {
      if (sum === 0) {
        sum = 1;
        result = path;
      } else {
        for (let i = 0; i < len; i++) {
          if (path[i] < result[i]) {
            result = path;
            sum = 1;
            break;
          } else if (path[i] > result[i]) {
            sum = 0;
            break;
          }
        }
      }
    } else {
      for (let [dx, dy] of directions) {
        let nx = x + dx;
        let ny = y + dy;
        if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx * N + ny]) {
          visited[nx * N + ny] = true;
          queue.push([nx, ny, path.concat(grid[nx][ny]), len + 1]);
        }
      }
    }
  }

  return result;
}