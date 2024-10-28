  let count = 0;
  let total = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      total += grid[i][j];
    }
  }
  while (total > 0) {
    count++;
    total -= capacity;
  }
  return count;
}
// Test cases
console.log(maxFill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)); // 6
console.log(maxFill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)); // 5
console.log(maxFill([[0,0,0], [0,0,0]], 5)); // 0
// Output: 6
// Output: 5
// Output: 0
// These test cases are based on the provided examples
// The output should be the number of times the buckets need to be lowered to empty the wells
// The code will calculate this by first calculating the total amount of water in all wells
// Then, it will subtract the bucket capacity from this total until it becomes 0 or less
// The number of times this is done is the number of times the buckets need to be lowered
// This code assumes that the grid is a 2D array where each element is either 0 or 1, representing an empty or filled well respectively
// It also assumes that the bucket capacity is a positive integer
// The function returns the number of times the buckets need to be lowered as an integer
// This function can be optimized by using a while loop instead of a for loop
// It can also be optimized by using a variable to keep track of the total amount of water in the wells, instead of recalculating it for each well
// It can also be optimized by using a variable to keep track of the amount of water left in the wells after each iteration of the while loop
// The time complexity of this function is O(n*m), where n is the number of rows in the grid and m is the number of columns in the grid
// The space complexity of this function is O(1), as it only uses a constant amount of space to store the variables and the grid
