  let minPath = [];
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      let path = [];
      let visited = new Set();
      dfs(grid, i, j, k, path, visited);
      if (minPath.length === 0 || isLessThan(minPath, path)) {
        minPath = path;
      }
    }
  }
  return minPath;

  function dfs(grid, i, j, k, path, visited) {
    if (k === 0) {
      return;
    }
    path.push(grid[i][j]);
    visited.add(`${i},${j}`);
    for (let x = i - 1; x <= i + 1; x++) {
      for (let y = j - 1; y <= j + 1; y++) {
        if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length && !visited.has(`${x},${y}`)) {
          dfs(grid, x, y, k - 1, path, visited);
        }
      }
    }
    path.pop();
    visited.delete(`${i},${j}`);
  }

  function isLessThan(pathA, pathB) {
    for (let i = 0; i < pathA.length; i++) {
      if (pathA[i] < pathB[i]) {
        return true;
      } else if (pathA[i] > pathB[i]) {
        return false;
      }
    }
    return false;
  }
};
// test the function
console.log(minPath([[1,2,3],[4,5,6],[7,8,9]], 3)); // [1, 2, 1]
console.log(minPath([[5,9,3],[4,1,6],[7,8,2]], 1)); // [1]  */

