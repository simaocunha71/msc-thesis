Here is a JavaScript solution for the problem:

```javascript
const carRaceCollision = (n) => {
  let collisionCount = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (i !== j) {
        if (Math.floor(i / j) === i / j) {
          collisionCount++;
        }
      }
    }
  }
  return collisionCount;
};
```

The logic behind this function is that for each pair of cars (i and j), we check if the ratio of i to j is an integer. If it is, then the cars will collide. We add up the number of such collisions for all pairs of cars. This function takes into account that cars are infinitely sturdy and strong, as they continue moving in their trajectory after a collision. The function returns the total number of collisions.

Please note that the time complexity of this function is O(n^2), as it has two nested loops that run n times each. This may not be efficient for large values of n. However, for small values of n, this function should work fine. If you need a more efficient solution, you can consider using a different approach, such as using a hash map to store the pairs of cars that will collide.