This problem can be solved by using the concept of relative velocity. Since the cars are moving in opposite directions, their relative velocity is the sum of their speeds. In this case, the relative velocity is 2 times the speed of a car (since there are two sets of cars moving in opposite directions).

The distance between the two sets of cars is initially very large, and the cars are moving in the same speed. As a result, the distance between the two sets of cars decreases at a rate of 2 times the speed of a car. Therefore, the number of collisions is equal to the initial distance divided by the relative velocity.

Here is the implementation of the function in JavaScript:

```javascript
const carRaceCollision = (n) => {
  const speed = 1; // speed of a car
  const relativeVelocity = 2 * speed; // relative velocity
  const initialDistance = n * speed; // initial distance between the two sets of cars
  const time = initialDistance / relativeVelocity; // time it takes for the two sets of cars to collide
  const numberOfCollisions = time / speed; // number of collisions
  return numberOfCollisions;
}
```

The function takes an argument `n`, which represents the number of cars in each set. It returns the number of collisions between the two sets of cars.