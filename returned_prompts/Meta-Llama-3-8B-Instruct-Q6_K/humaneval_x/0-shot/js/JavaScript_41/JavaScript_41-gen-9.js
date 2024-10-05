Here is a JavaScript function to solve the problem:

```javascript
const carRaceCollision = (n) => {
  let collisions = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (i !== j && Math.floor((i + j) / 2) === j) {
        collisions++;
      }
    }
  }
  return collisions;
};
```

This function uses two nested loops to iterate over all pairs of cars. For each pair, it checks if the cars collide by comparing their speeds. If the cars collide, it increments the `collisions` counter. Finally, it returns the total number of collisions.

This solution has a time complexity of O(n^2) because it uses two nested loops to iterate over all pairs of cars. The space complexity is O(1) because it only uses a constant amount of space to store the `collisions` counter.