You can use the formula for the sum of the first n natural numbers to solve this problem.

The formula for the sum of the first n natural numbers is:

```
sum = n * (n + 1) / 2
```

In this case, you want to find the number of collisions for n cars driving left to right and n cars driving right to left. Since the cars are moving in opposite directions, each car from the left will collide with each car from the right. Therefore, the number of collisions is simply the square of n.

Here's the code:

```javascript
const carRaceCollision = (n) => {
  return n * n;
};
```

This function takes an integer n as input and returns the number of collisions.