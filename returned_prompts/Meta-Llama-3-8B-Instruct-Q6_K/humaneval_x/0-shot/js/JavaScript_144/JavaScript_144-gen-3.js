Here is a JavaScript function that simplifies the fraction representation of two numbers and checks if the result is an integer:

```javascript
const simplify = (x, n) => {
  const [xN, xD] = x.split('/').map(Number);
  const [nN, nD] = n.split('/').map(Number);
  const gcd = (a, b) => (b === 0) ? a : gcd(b, a % b);
  const commonGcd = gcd(xD * nD, xN * nN);
  return (xN * nD) / commonGcd === (xN / gcd(xN, commonGcd)) * (nD / gcd(nD, commonGcd));
};
```
Here's how this function works:

1. It splits the input strings into their numerator and denominator parts using the `/` character as a separator.
2. It converts the numerator and denominator parts into numbers using the `map` function.
3. It calculates the greatest common divisor (GCD) of the numerator and denominator parts of both fractions using the `gcd` function.
4. It calculates the common GCD of the numerator and denominator parts of both fractions by multiplying the numerator and denominator parts of both fractions and then dividing by the GCD.
5. It checks if the result of the multiplication and division is an integer by comparing it to the result of the division of the numerator and denominator parts of both fractions by their respective GCDs.

The function returns `true` if the result is an integer and `false` otherwise. This function can be used to simplify the fraction representation of two numbers and check if the result is an integer. For example, the function `simplify("1/5", "5/1")` returns `true` because the result of the multiplication and