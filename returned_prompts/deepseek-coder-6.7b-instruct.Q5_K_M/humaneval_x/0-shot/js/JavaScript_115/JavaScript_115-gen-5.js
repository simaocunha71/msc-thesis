  let buckets = 0
  let total = 0

  for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[i].length; j++) {
          if (grid[i][j] === 1) {
              total++
          }
      }
  }
  
  while (total > 0) {
      buckets++
      total -= capacity
  }

  return buckets
}

console.log(maxFill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)) // 6
console.log(maxFill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)) // 5
console.log(maxFill([[0,0,0], [0,0,0]], 5)) // 0
```

In this solution, we first count the total number of 1s in the grid, which represents the total amount of water in all the wells. Then, we use a while loop to continuously lower the buckets by the capacity until all the water is gone. The number of times we lower the buckets is the result.

This solution has a time complexity of O(n*m) because we have to traverse the entire grid to count the total number of water units. The space complexity is O(1) because we only use a constant amount of space to store the count of buckets and the total amount of water.

This solution assumes that the grid and bucket capacity are always valid, and that the capacity is always greater than 0.
*/

const maxFill = (grid, capacity) => {
  let buckets = 0
  let total = 0

  for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[i].length; j++) {
          if (grid[i][j] === 1) {
              total++
          }
      }
  }
  
  while (total > 0) {
      buckets++
      total