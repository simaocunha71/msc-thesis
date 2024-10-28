```javascript
const greatestCommonDivisor = (a, b) => {
  if (b === 0) return a;
  return greatestCommonDivisor(b, a % b);
};
```

Explanation:
The function `greatestCommonDivisor` takes two integers `a` and `b` as input. It uses the Euclidean algorithm to find the greatest common divisor (GCD) of the two numbers.

The base case of the recursion is when `b` is 0. In this case, the GCD is `a`.

Otherwise, the function calls itself with `b` and the remainder of `a` divided by `b` as arguments. This is because the GCD of `a` and `b` is the same as the GCD of `b` and the remainder of `a` divided by `b`. This process is repeated until `b` is 0, at which point the GCD is returned.

For example, if we call `greatestCommonDivisor(25, 15)`, the function will recursively call itself as follows:

* `greatestCommonDivisor(25, 15)` calls `greatestCommonDivisor(15, 25 % 15)`
* `greatestCommonDivisor(15, 10)` calls `greatestCommonDivisor(10, 15 % 10)`
* `greatestCommonDivisor(10, 5)` calls `greatestCommonDivisor(5, 10 % 5)`
* `greatestCommonDivisor(5, 0)` returns 5, which is the GCD of 25 and 15.

This approach ensures that the GCD is found efficiently, with a time complexity of O(log min(a, b)).