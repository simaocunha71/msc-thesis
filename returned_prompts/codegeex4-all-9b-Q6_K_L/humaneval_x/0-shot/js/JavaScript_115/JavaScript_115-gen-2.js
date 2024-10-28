To solve this problem, we can iterate through each row of the grid and calculate the number of buckets needed to empty the well. We can then add up the total number of buckets needed for all wells.

Here is the JavaScript code to solve the problem:

```javascript
const maxFill = (grid, capacity) => {
  let buckets = 0;

  for (let i = 0; i < grid.length; i++) {
    let water = 0;

    for (let j = 0; j < grid[i].length; j++) {
      water += grid[i][j];
    }

    buckets += Math.ceil(water / capacity);
  }

  return buckets;
}
```

This code works by iterating through each row of the grid and calculating the total amount of water in the well. It then divides the total amount of water by the bucket capacity and takes the ceiling of the result to ensure that all water is accounted for. Finally, it adds up the total number of buckets needed for all wells and returns the result.