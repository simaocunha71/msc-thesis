};

*/

const minPath = (grid, k) => {
  const n = grid.length;
  const directions = [
    [-1, 0],
    [0, -1],
    [0, 1],
    [1, 0],
  ];

  const getNeighbors = ([x, y]) =>
    directions
      .map(([dx, dy]) => [x + dx, y + dy])
      .filter(([nx, ny]) => nx >= 0 && nx < n && ny >= 0 && ny < n);

  const visit = (coord, rest, path) => {
    if (rest === 0) return path;
    let minPath = null;
    for (let next of getNeighbors(coord)) {
      const nextPath = visit(
        next,
        rest - 1,
        path.concat(grid[next[0]][next[1]])
      );
      if (minPath === null || compare(nextPath, minPath) < 0) {
        minPath = nextPath;
      }
    }
    return minPath;
  };

  const compare = (a, b) => {
    for (let i = 0; i < a.length; ++i) {
      if (a[i] < b[i]) return -1;
      if (a[i] > b[i]) return 1;
    }
    return 0;
  };

  let minPath = null;
  for (let x = 0; x < n; ++x)
    for (let y = 0; y < n; ++y) {
      const path = visit([x, y], k - 1, [grid[x][y]]);
      if (minPath === null || compare(path, minPath) < 0) {
        minPath = path;
      }
    }

  return minPath;
};

module.exports = minPath;
