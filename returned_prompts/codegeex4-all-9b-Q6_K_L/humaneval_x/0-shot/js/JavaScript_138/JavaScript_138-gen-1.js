Here is the solution in JavaScript:

```javascript
const isEqualToSumEven = (n) => {
  if (n % 2 != 0) {
    return false;
  }
  if (n >= 8) {
    return true;
  }
  return false;
};
```

The function `isEqualToSumEven` first checks if the number `n` is odd. If it is, it returns `false` because an odd number cannot be written as the sum of four even numbers. If the number is even, it then checks if it is greater than or equal to 8. If it is, it returns `true` because any even number greater than or equal to 8 can be written as the sum of four even numbers. If the number is less than 8, it returns `false`.