Here is a JavaScript function that calculates the number of collisions for a given number of cars `n`:
```javascript
const carRaceCollision = (n) => {
  let collisions = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i !== j && Math.abs(i - j) % 2 === 1) {
        collisions++;
      }
    }
  }
  return collisions / 2; // since each collision is counted twice
};
```
Here's an explanation of the algorithm:

1. Initialize a variable `collisions` to 0, which will count the number of collisions.
2. Loop through each car `i` from 0 to `n-1`.
3. For each car `i`, loop through each car `j` from 0 to `n-1`, excluding `i` itself (since a car cannot collide with itself).
4. Check if `i` and `j` are on opposite sides of the road by checking if the absolute difference between `i` and `j` is odd. If it is, then they are on opposite sides and can collide.
5. If `i` and `j` can collide, increment the `collisions` count.
6. Since each collision is counted twice (once for each car involved), divide the total count by 2 at the end to get the correct number of collisions.

For example, if `n` is 4, the function will return 2, since there are 2 collisions: car 0 (moving left) collides with car 3 (moving right), and car 1 (moving left) collides with car 2 (moving right).