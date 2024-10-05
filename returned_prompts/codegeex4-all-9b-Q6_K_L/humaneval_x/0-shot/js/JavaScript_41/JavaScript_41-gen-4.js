The function carRaceCollision(n) can be implemented as follows:

```javascript
const carRaceCollision = (n) => {
  return Math.pow(n, 2);
}
```

Explanation:
Since the cars are moving in opposite directions, every car moving left to right will collide with every car moving right to left. Therefore, the number of collisions will be the product of the number of cars moving left to right and the number of cars moving right to left, which is n * n = n^2.