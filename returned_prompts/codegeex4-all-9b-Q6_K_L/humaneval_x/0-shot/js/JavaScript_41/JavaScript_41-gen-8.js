This is a simple problem that can be solved using the principles of probability and combinatorics. The key insight is that the number of collisions is equal to the number of ways in which two cars can be chosen from the total of 2n cars such that one is moving left to right and the other is moving right to left.

The number of ways to choose 2 cars from a set of 2n cars is given by the combination formula:

C(n, k) = n! / (k!(n-k)!)

where n is the total number of items, k is the number of items to choose, and ! denotes the factorial function.

In this case, n = 2n and k = 2, so the number of collisions is:

C(2n, 2) = (2n)! / (2!(2n-2)!)

Simplifying this expression, we get:

C(2n, 2) = (2n)(2n-1) / 2

This formula can be implemented in JavaScript as follows:

```javascript
const carRaceCollision = (n) => {
  return (2*n) * (2*n - 1) / 2;
}
```

This function takes an integer n as input and returns the number of collisions that will occur in the car race.