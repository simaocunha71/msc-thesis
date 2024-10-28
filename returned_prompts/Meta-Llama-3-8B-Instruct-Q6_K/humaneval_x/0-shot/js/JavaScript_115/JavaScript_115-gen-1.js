```
function maxFill(grid, capacity) {
  let count = 0;
  for (let i = 0; i < grid.length; i++) {
    let water = 0;
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        water += 1;
      } else {
        water = 0;
      }
      while (water > 0 && water >= capacity) {
        water -= capacity;
        count += 1;
      }
    }
  }
  return count;
}
```
Explanation: 
We iterate over each well in the grid. For each well, we keep track of the amount of water in it. When the water level exceeds the bucket capacity, we lower the bucket and add the bucket's capacity to the count. We keep doing this until the water level is less than or equal to the bucket capacity. This way, we ensure that we empty the well completely. We repeat this process for each well and return the total count.

Note: This solution assumes that the bucket capacity is a constant and is not provided as an input. If the bucket capacity is variable, the problem statement should be modified to include it. 

Time Complexity: O(m*n), where m is the number of wells and n is the length of each well.

Space Complexity: O(1), as we only use a constant amount of space to store the count and water level. 