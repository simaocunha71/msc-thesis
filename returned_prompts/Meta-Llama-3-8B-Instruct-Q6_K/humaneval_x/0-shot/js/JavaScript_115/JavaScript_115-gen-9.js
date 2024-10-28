Here is a JavaScript solution using a simple loop to iterate over each well and a counter to keep track of the number of times the bucket needs to be lowered:

```javascript
const maxFill = (grid, capacity) => {
  let count = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        count += Math.ceil(grid[i][j] / capacity);
      }
    }
  }
  return count;
};
```

In this function, `grid` is the 2D array representing the wells and `capacity` is the capacity of the bucket. The function initializes a counter `count` to 0, then loops over each well in the grid. For each well, it checks if the well is filled (i.e., `grid[i][j] === 1`). If the well is filled, it calculates the number of times the bucket needs to be lowered to empty the well using the formula `Math.ceil(grid[i][j] / capacity)`, where `Math.ceil` rounds up to the nearest integer. It then adds this number to the `count`. Finally, it returns the `count`, which represents the number of times the bucket needs to be lowered to empty all the wells.