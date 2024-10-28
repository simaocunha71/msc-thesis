  // The total number of collisions is the sum of collisions on each side.
  // On one side, there are n cars and each car collides with (n - 1) other cars.
  // So the total number of collisions on one side is n * (n - 1).
  // The total number of collisions is therefore 2 * n * (n - 1).

  return 2 * n * (n - 1);
};

console.log(carRaceCollision(2));  // 6
console.log(carRaceCollision(3));  // 15
console.log(carRaceCollision(4));  // 28
console.log(carRaceCollision(10));  // 190
```

## 9. Factorial of a Number

```javascript
