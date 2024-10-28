  var directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
  var n = grid.length;
  var flatGrid = grid.flat();
  flatGrid.sort((a, b) => a - b);

  var result = [];
  var minDist = Number.MAX_SAFE_INTEGER;
  var visited = Array(n * n).fill(false);

  const dfs = (pos, depth, dist) => {
    if (depth === k) {
      if (dist < minDist) {
        minDist = dist;
        result = [...pos];
      }
      return;
    }
    for (let i = 0; i < n * n; ++i) {
      if (visited[i]) continue;
      let [x, y] = [Math.floor(i / n), i % n];
      let [dx, dy] = [pos[pos.length - 1][0] - x, pos[pos.length - 1][1] - y];
      if (Math.abs(dx) + Math.abs(dy) > 1) continue;
      visited[i] = true;
      pos.push([x, y]);
      dfs(pos, depth + 1, dist + flatGrid[i]);
      pos.pop();
      visited[i] = false;
    }
  };

  for (let i = 0; i < n * n; ++i) {
    visited[i] = true;
    dfs([[Math.floor(i / n), i % n]], 1, flatGrid[i]);
    visited[i] = false;
  }

  return result.map(cell => grid[cell[0]][cell[1]]);
};



