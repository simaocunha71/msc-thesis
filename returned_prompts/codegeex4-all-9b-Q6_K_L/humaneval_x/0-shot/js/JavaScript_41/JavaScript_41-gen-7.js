This problem can be solved by counting the number of pairs of cars that can potentially collide. Since the cars are moving at the same speed, the only thing that matters is their relative positions. Two cars can collide if the car moving left to right is to the right of the car moving right to left. There are n cars moving left to right and n cars moving right to left, so there are n choose 2 = n(n-1)/2 pairs of cars that can potentially collide. The function can be implemented as follows:

```javascript
const carRaceCollision = (n) => {
  return n * (n - 1) / 2;
}
```

This function takes an integer n as input and returns the number of potential collisions. For example, if there are 5 cars, the function would return 10, since there are 5 choose 2 = 10 pairs of cars that can potentially collide.