
}
*/

const grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]];
const capacity = 1;
console.log(maxFill(grid, capacity)); // 6

const grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]];
const capacity2 = 2;
console.log(maxFill(grid2, capacity2)); // 5

const grid3 = [[0,0,0], [0,0,0]];
const capacity3 = 5;
console.log(maxFill(grid3, capacity3)); // 0

// Answer:

const maxFill = (grid, capacity) => {
  let buckets = 0;
  const flatGrid = grid.flat();

  for(let i = 0; i < flatGrid.length; i++){
    if(flatGrid[i] === 1){
      buckets++;
    }
  }

  return Math.ceil(buckets / capacity);
}

// Time Complexity = O(m*n) 
// where m = number of rows in the grid 
// and n = number of columns in the grid.
// This is because we need to traverse the whole grid to count the total number of water wells.

// Space Complexity = O(m*n) 
// because we are storing the grid in a flattened array.
// It will be a flattened version of grid in memory.

// This is a linear solution, and it should work for the given constraints.

// The Math.ceil function is used to round up the result, so if there are leftover water wells that do not fill up the bucket, we will need one more bucket to empty them.

// This solution assumes that the capacity of the bucket is always an integer, and that the grid is always a 2D array.

// The solution assumes that the grid is a rectangular grid of wells, where each well is represented by a 1 in the grid.

// The solution also assumes that the grid is a 2D array