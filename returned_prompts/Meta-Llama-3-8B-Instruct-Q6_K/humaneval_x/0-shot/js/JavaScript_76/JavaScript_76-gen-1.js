The function isSimplePower should take two parameters, x and n, and return a boolean value indicating whether x is a simple power of n.

Here is a possible implementation of the function:
```
const isSimplePower = (x, n) => {
  return Math.log(x) / Math.log(n) % 1 === 0;
};
```
This function uses the mathematical property that the logarithm of a power is the logarithm of the base raised to the power of the exponent. It calculates the logarithm of x to the base n, and checks if the result is an integer by taking the remainder of the division by 1. If the remainder is 0, then x is a simple power of n, and the function returns true. Otherwise, it returns false.

Here are some examples of how this function can be used:
```
console.log(isSimplePower(1, 4)); // true
console.log(isSimplePower(2, 2)); // true
console.log(isSimplePower(8, 2)); // true
console.log(isSimplePower(3, 2)); // false
console.log(isSimplePower(3, 1)); // false
console.log(isSimplePower(5, 3)); // false
```
I hope this helps! Let me know if you have any questions.