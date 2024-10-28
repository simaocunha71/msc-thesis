Here is the solution to the problem:
```
const greatestCommonDivisor = (a, b) => {
  if (b === 0) {
    return a;
  }
  return greatestCommonDivisor(b, a % b);
};
```
This function uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers `a` and `b`. The algorithm works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is 0. At that point, `a` is the GCD of the original `a` and `b`. The function is recursive, meaning it calls itself with the new values of `a` and `b` until the base case is reached.

For example, if we call `greatestCommonDivisor(3, 5)`, the function will recursively call itself as follows:
```
greatestCommonDivisor(3, 5) => greatestCommonDivisor(5, 3)
                           => greatestCommonDivisor(3, 2)
                           => greatestCommonDivisor(2, 1)
                           => greatestCommonDivisor(1, 0)
```
At this point, `b` is 0, so the function returns `a`, which is 1. Therefore, the GCD of 3 and 5 is 1.

Similarly, if we call `greatestCommonDivisor(25, 15)`, the function will recursively call itself as follows:
```
greatestCommonDivisor(25, 15) => greatestCommonDivisor(15, 10)
                           => greatestCommonDivisor(10, 5)
                           => greatestCommonDivisor(5, 5)
                           => greatestCommonDivisor(5, 0)
```
At this point, `b` is 0, so the function returns `a`, which is 5. Therefore, the GCD of 25 and 15 is 5.