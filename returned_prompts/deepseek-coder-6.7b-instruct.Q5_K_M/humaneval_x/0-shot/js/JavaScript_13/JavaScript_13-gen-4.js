  if (b == 0) 
    return a;
  else 
    return greatestCommonDivisor(b, a % b);
};
```

The `greatestCommonDivisor` function uses the Euclidean algorithm to find the greatest common divisor of two numbers. The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.

## Problem: Fibonacci Number

Write a JavaScript function that generates the nth Fibonacci number.

```javascript
