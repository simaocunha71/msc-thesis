Here is the JavaScript code that solves the problem:

```javascript
const simplify = (x, n) => {
  const [numeratorX, denominatorX] = x.split('/');
  const [numeratorN, denominatorN] = n.split('/');

  const numerator = parseInt(numeratorX) * parseInt(denominatorN);
  const denominator = parseInt(denominatorX) * parseInt(denominatorN);

  if (gcd(denominator, numerator) !== 1) {
    return false;
  }

  return true;
};

function gcd(a, b) {
  while (b !== 0) {
    const temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```
This code splits the input strings into their numerator and denominator parts, then calculates the product of the numerators and the product of the denominators. It then checks if the greatest common divisor (GCD) of the denominator and the numerator is 1. If it is not 1, the function returns false, indicating that the expression does not evaluate to a whole number. If the GCD is 1, the function returns true, indicating that the expression does evaluate to a whole number.

The `gcd` function calculates the GCD of two numbers using the Euclidean algorithm. It repeatedly replaces `a` with the remainder of `a` divided by `b`, and `b` with the previous value of `a`. The loop continues until `b` is 0, at which point `a` is the GCD of the original `a` and `b`.  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */  */