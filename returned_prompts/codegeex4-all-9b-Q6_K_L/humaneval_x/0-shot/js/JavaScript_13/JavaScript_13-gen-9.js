```js
const greatestCommonDivisor = (a, b) => {
  if (b === 0) {
    return a;
  }
  return greatestCommonDivisor(b, a % b);
};
```

This function uses the Euclidean algorithm to find the greatest common divisor of two integers. The algorithm works by repeatedly replacing the larger number with the remainder of the two numbers until the remainder is 0. At that point, the other number is the greatest common divisor.