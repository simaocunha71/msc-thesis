  // Initialize the grid size
  const n = grid.length;

  // Initialize the result array
  let res = [];

  // Initialize the directions array
  const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];

  // Initialize the minimum path length
  let minLen = Infinity;

  // Helper function to get neighbor cells
  const getNeighbors = (x, y) => {
    let neighbors = [];
    for (let i = 0; i < dirs.length; i++) {
      let nx = x + dirs[i][0], ny = y + dirs[i][1];
      if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
        neighbors.push([nx, ny]);
      }
    }
    return neighbors;
  };

  // Helper function to backtracking
  const backtrack = (x, y, k, path) => {
    // Base case
    if (k === 0) {
      // Check if this path is the minimum
      if (path.length < minLen) {
        minLen = path.length;
        res = [...path];
      }
      return;
    }
    // Get all neighbors
    let neighbors = getNeighbors(x, y);
    for (let i = 0; i < neighbors.length; i++) {
      let nx = neighbors[i][0], ny = neighbors[i][1];
      // Add the current cell value to the path
      path.push(grid[nx][ny]);
      // Backtracking
      backtrack(nx, ny, k - 1, path);
      // Remove the current cell value from the path
      path.pop();
    }
  };

  // Start from each cell in the grid
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      backtrack(i, j, k - 1, [grid[i][j]