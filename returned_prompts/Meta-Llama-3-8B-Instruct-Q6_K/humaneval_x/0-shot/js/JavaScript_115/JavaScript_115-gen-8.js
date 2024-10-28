Here is a possible solution in JavaScript:
```
function maxFill(grid, capacity) {
  let count = 0;
  for (let i = 0; i < grid.length; i++) {
    let water = 0;
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        water += 1;
      }
    }
    count += Math.ceil(water / capacity);
  }
  return count;
}
```
The function `maxFill` takes two parameters: `grid` which is a 2D array representing the wells and `capacity` which is the capacity of the buckets.

The function iterates over each row of the grid, and for each row, it counts the number of units of water in that row. It then adds the ceiling of the water divided by the capacity to the count. This is because the buckets can only hold a certain amount of water, so we need to round up to the nearest whole number.

Finally, the function returns the total count of times the buckets need to be lowered.

You can test this function with the examples you provided:
```
console.log(maxFill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)); // Output: 6
console.log(maxFill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)); // Output: 5
console.log(maxFill([[0,0,0], [0,0,0]], 5)); // Output: 0
```
Note that this solution assumes that the buckets can be filled and emptied independently, and that the capacity of the buckets is the same for all wells. If this is not the case, the solution may need to be modified accordingly.