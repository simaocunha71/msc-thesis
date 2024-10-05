This problem can be solved by considering the fact that each car moving from left to right will collide with all the cars moving from right to left. So, the total number of collisions will be the product of the number of cars moving from left to right and the number of cars moving from right to left.

Here is the implementation of the carRaceCollision function:

```javascript
const carRaceCollision = (n) => {
  return n * n;
};
```

The time complexity of this solution is O(1) because it only involves a simple multiplication operation.