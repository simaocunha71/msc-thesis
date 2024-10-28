  var result = [];
  var n = grid.length;
  var visited = Array.from({length: n}, () => Array(n).fill(false));
  var minPathSum = Infinity;
  var directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];

  const dfs = (x, y, k, pathSum) => {
    if (k === 0) {
      if (pathSum < minPathSum) {
        minPathSum = pathSum;
        result = [...path];
      }
      return;
    }

    for (let i = 0; i < 4; i++) {
      let newX = x + directions[i][0];
      let newY = y + directions[i][1];
      if (newX >= 0 && newX < n && newY >= 0 && newY < n && !visited[newX][newY]) {
        visited[newX][newY] = true;
        path.push(grid[newX][newY]);
        dfs(newX, newY, k - 1, pathSum + grid[newX][newY]);
        visited[newX][newY] = false;
        path.pop();
      }
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      path = [grid[i][j]];
      visited[i][j] = true;
      dfs(i, j, k - 1, grid[i][j]);
      visited[i][j] = false;
      path.pop();
    }
  }

  return result;
}



