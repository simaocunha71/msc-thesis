The task is to implement a function that will simplify the expression x * n. The function returns true if x * n evaluates to a whole number and false otherwise. Both x and n are string representation of a fraction, and have the following format, <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

We can solve this problem by parsing the fractions, multiplying them, and then checking if the result is an integer. Here is the JavaScript function that implements this:

```javascript
const simplify = (x, n) => {
  const [xNumerator, xDenominator] = x.split('/').map(Number);
  const [nNumerator, nDenominator] = n.split('/').map(Number);
  
  const numerator = xNumerator * nNumerator;
  const denominator = xDenominator * nDenominator;
  
  if (gcd(denominator, numerator) !== 1) return false;
  return true;
};

function gcd(a, b) {
  if (b === 0) return a;
  return gcd(b, a % b);
}
```

This function first parses the input strings into their numerator and denominator parts. It then multiplies the numerators and denominators together to get the result of the multiplication. It then checks if the result is an integer by checking if the greatest common divisor (GCD) of the denominator and the numerator is 1. If it is, the function returns true; otherwise, it returns false. The GCD is calculated using the Euclidean algorithm. 

The function works by repeatedly replacing a and b with b and the remainder of a divided by b, until b is 0. At that point, a is the GCD of the original a and b. 

This function assumes that the input strings are valid fractions, and that the denominators are not zero. It also assumes that the input strings are in the format <numerator>/<denominator>, where both numerator and denominator are positive whole numbers. If the input strings are not in this format, or if the denominators are zero, the function may not work correctly.  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */