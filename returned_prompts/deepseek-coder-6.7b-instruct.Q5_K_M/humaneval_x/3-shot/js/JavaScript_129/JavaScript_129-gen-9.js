  const n = grid.length;
  const visited = Array.from({ length: n }, () => Array(n).fill(false));
  const minPathHelper = (i, j, k) => {
    if (k === 0) {
      return [];
    }
    let min = null;
    for (let [dx, dy] of [[0, 1], [1, 0], [-1, 0], [0, -1]]) {
      let x = i + dx, y = j + dy;
      if (x >= 0 && x < n && y >= 0 && y < n && !visited[x][y]) {
        visited[x][y] = true;
        let path = [grid[i][j]].concat(minPathHelper(x, y, k - 1));
        if (min === null || compare(path, min) < 0) {
          min = path;
        }
        visited[x][y] = false;
      }
    }
    return min;
  };
  let min = null;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      visited[i][j] = true;
      let path = minPathHelper(i, j, k - 1);
      if (min === null || compare(path, min) < 0) {
        min = path;
      }
      visited[i][j] = false;
    }
  }
  return min;
};

const compare = (a, b) => {
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) return a[i] < b[i] ? -1 : 1;
  }
  return 0;
}

