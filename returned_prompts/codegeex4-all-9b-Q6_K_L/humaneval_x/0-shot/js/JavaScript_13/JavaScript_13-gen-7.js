The greatest common divisor (GCD) of two numbers is the largest number that divides both of them without leaving a remainder. One of the ways to find the GCD of two numbers is using the Euclidean algorithm. Here is a JavaScript function that calculates the GCD of two integers using this algorithm:

```javascript
const greatestCommonDivisor = (a, b) => {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```

This function uses a while loop to repeatedly calculate the remainder of `a` divided by `b` and assign `b` to `a` and `a % b` to `b` until `b` becomes `0`. At this point, `a` will be the GCD of the original `a` and `b`.

Here are some examples of how to use this function:

```javascript
console.log(greatestCommonDivisor(3, 5));  // Output: 1
console.log(greatestCommonDivisor(25, 15));  // Output: 5
```