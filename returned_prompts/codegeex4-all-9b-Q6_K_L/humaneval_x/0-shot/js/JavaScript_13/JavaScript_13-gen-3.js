The greatest common divisor (GCD) of two integers a and b is the largest integer that divides both of them without leaving a remainder.

The GCD can be found using the Euclidean algorithm, which is based on the principle that the GCD of two numbers also divides their difference.

Here is a JavaScript function that implements the Euclidean algorithm to find the GCD of two integers:

```javascript
const greatestCommonDivisor = (a, b) => {
  // Ensure a is always greater than or equal to b
  if (a < b) {
    [a, b] = [b, a];
  }

  // If b is 0, a is the GCD
  if (b === 0) {
    return a;
  }

  // Otherwise, recursively call the function with the difference between a and b
  return greatestCommonDivisor(a - b, b);
};
```

This function works by repeatedly subtracting the smaller number from the larger one until the remainder is 0. At that point, the other number is the GCD.