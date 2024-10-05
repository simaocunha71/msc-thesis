You can use a while loop to simulate the movement of the cars and count the number of collisions. Here's the code:

```javascript
const carRaceCollision = (n) => {
  let leftCars = 1;
  let rightCars = 1;
  let collisions = 0;

  while (leftCars <= n && rightCars <= n) {
    if (leftCars < rightCars) {
      leftCars++;
    } else if (leftCars > rightCars) {
      rightCars++;
    } else {
      collisions++;
      leftCars++;
      rightCars++;
    }
  }

  return collisions;
};
```

This function initializes two variables, `leftCars` and `rightCars`, to keep track of the number of cars moving left and right, respectively. It also initializes a variable `collisions` to keep track of the number of collisions.

The while loop runs until both `leftCars` and `rightCars` exceed `n`. Inside the loop, it checks if the number of left-moving cars is less than the number of right-moving cars. If it is, it increments `leftCars` by 1. If it's greater, it increments `rightCars` by 1. If they're equal, it increments both `collisions` and both `leftCars` and `rightCars` by 1, indicating a collision.

Finally, the function returns the number of collisions.