Here is the solution for the problem:

```javascript
const carRaceCollision = (n) => {
  let collisions = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (i !== j && i + j === n + 1) {
        collisions++;
      }
    }
  }
  return collisions;
};
```

The solution works by iterating over all pairs of cars and checking if they collide. Two cars collide if their total distance from the starting point is equal to the total number of cars. This is because there are `n` cars driving left to right and `n` cars driving right to left, so the total number of cars is `2 * n`. The distance from the starting point for each car is equal to its position, so the total distance for two cars to collide is `n`.

In the code, we use two nested loops to iterate over all pairs of cars. We check if the sum of the distances for each car is equal to the total number of cars, and if so, we increment the collision count. Finally, we return the total number of collisions.

This solution has a time complexity of O(n^2), where n is the number of cars. This is because we need to iterate over all pairs of cars to check for collisions. The space complexity is O(1), as we only use a constant amount of space to store the collision count.