// Initialize an empty array to store the result
let result = [];

// Iterate over the grid to find the minimum path
for (let i = 0; i < grid.length; i++) {
  for (let j = 0; j < grid[i].length; j++) {
    // Check if the current cell is the starting point
    if (i === 0 && j === 0) {
      // Start the path from the top-left cell
      result.push(grid[i][j]);
      for (let pathLength = 1; pathLength <= k; pathLength++) {
        // Find the next cell in the path
        let nextCell = findNextCell(grid, i, j, pathLength, result);
        if (nextCell) {
          // Add the value of the next cell to the result
          result.push(nextCell);
          // Check if the path has reached the desired length
          if (result.length === k) {
            return result;
          }
        } else {
          // If no next cell is found, break the loop
          break;
        }
      }
    }
  }
}

// Function to find the next cell in the path
function findNextCell(grid, i, j, pathLength, result) {
  // Check the neighbors of the current cell
  let neighbors = getNeighbors(grid, i, j);
  // Sort the neighbors based on their values
  neighbors.sort((a, b) => a - b);
  // Check if the neighbors have been visited
  for (let neighbor of neighbors) {
    if (!result.includes(neighbor)) {
      // Add the neighbor to the result and return it
      result.push(neighbor);
      return neighbor;
    }
  }
  // If no unvisited neighbor is found, return null
  return null;
}

// Function to get the neighbors of a cell
function getNeighbors(grid, i, j) {
  let neighbors = [];
  // Check the top neighbor
  if (i > 0) {
    neighbors.push(grid[i - 1][j]);
  }
  // Check the bottom neighbor
  if (i < grid.length - 1) {
    neighbors.push(grid[i + 1][j]);
  }
  // Check the left neighbor
  if (j > 0) {
    neighbors.push(grid[i][j - 1]);
  }
  // Check the right neighbor
  if (j < grid[i].length - 