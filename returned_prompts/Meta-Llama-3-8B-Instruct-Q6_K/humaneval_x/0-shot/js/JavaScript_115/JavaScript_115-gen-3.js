Here is a JavaScript solution for the problem:

```javascript
const maxFill = (grid, capacity) => {
  let count = 0;
  for (let i = 0; i < grid.length; i++) {
    let water = 0;
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        water += 1;
      }
    }
    while (water > 0) {
      if (water >= capacity) {
        water -= capacity;
        count++;
      } else {
        count++;
        water = 0;
      }
    }
  }
  return count;
};
```

This solution iterates over each well in the grid, calculates the total amount of water in the well, and then uses a while loop to empty the well by lowering the bucket as many times as necessary. The bucket is lowered until it is either empty or has reached its capacity. The number of times the bucket is lowered is the number of times it needs to be lowered in total to empty the well. The function returns the total number of times the bucket needs to be lowered for all wells.