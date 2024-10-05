  let count = 0;
  for (let i = 0; i < grid.length; i++) {
    let water = 0;
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] == 1) {
        water += 1;
      } else {
        water = 0;
      }
      if (water > capacity) {
        count += water / capacity;
        water %= capacity;
      }
    }
  }
  return Math.ceil(count);
}
// Math.ceil is used because the problem statement asks for the minimum number of times the bucket needs to be lowered, and the bucket can be lowered a maximum of one time for each full bucket, even if it's not exactly full. Math.ceil ensures that the bucket is lowered at least once for each full bucket.