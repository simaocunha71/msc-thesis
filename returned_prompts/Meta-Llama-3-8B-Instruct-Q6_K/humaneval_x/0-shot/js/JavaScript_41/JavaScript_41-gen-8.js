Here is a possible solution in JavaScript:
```
const carRaceCollision = (n) => {
  let collisions = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (i !== j && Math.floor(i / j) === j) {
        collisions++;
      }
    }
  }
  return collisions;
};
```
The idea is to iterate over all pairs of cars (i, j) and check if they will collide. A collision occurs when the distance between two cars is equal to the speed of the car that's moving right to left (i.e., `j`). This is equivalent to checking if `i` is a multiple of `j`. If `i` is a multiple of `j`, it means that the car moving left to right will catch up to the car moving right to left at some point, resulting in a collision.

The outer loop iterates over the cars moving left to right, and the inner loop iterates over the cars moving right to left. We skip the case where `i === j` because a car cannot collide with itself.

Finally, we return the total number of collisions found.

You can test this function with different values of `n` to see the output. For example, `carRaceCollision(5)` should return `2`, because there are two possible collisions: `car 1 (moving left) collides with car 2 (moving right)`, and `car 2 (moving left) collides with car 3 (moving right)`.