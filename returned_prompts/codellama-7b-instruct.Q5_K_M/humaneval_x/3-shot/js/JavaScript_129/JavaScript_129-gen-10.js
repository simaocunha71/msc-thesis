  const n = grid.length;
  const min_path = new Array(n * n).fill(0);
  const visited = new Array(n * n).fill(false);

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      min_path[i * n + j] = grid[i][j];
    }
  }

  let min_path_size = 1;
  visited[0] = true;
  for (let i = 0; i < k; i++) {
    let new_min_path_size = 0;
    for (let j = 0; j < n * n; j++) {
      if (min_path[j] == 0) {
        continue;
      }
      for (let d = 0; d < 4; d++) {
        let new_x = j % n + directions[d][0];
        let new_y = Math.floor(j / n) + directions[d][1];
        if (0 <= new_x && new_x < n && 0 <= new_y && new_y < n && !visited[new_y * n + new_x] && min_path[new_y * n + new_x] > 0) {
          new_min_path_size += 1;
          min_path[new_y * n + new_x] = 0;
          visited[new_y * n + new_x] = true;
        }
      }
    }

    if (min_path_size == new_min_path_size) {
      break;
    }
    min_path_size = new_min_path_size;
  }

  return min_path.filter((e) => e > 0);
}



