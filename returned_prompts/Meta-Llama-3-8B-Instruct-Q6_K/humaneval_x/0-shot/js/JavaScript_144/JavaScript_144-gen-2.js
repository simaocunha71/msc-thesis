```javascript
const simplify = (x, n) => {
  const [xNumerator, xDenominator] = x.split('/').map(Number);
  const [nNumerator, nDenominator] = n.split('/').map(Number);

  const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);

  const numerator = xNumerator * nDenominator;
  const denominator = xDenominator * nNumerator;

  const commonGcd = gcd(numerator, denominator);

  return numerator / commonGcd === denominator / commonGcd;
};
```


Explanation:

1. We first split the input strings into their respective numerators and denominators using the `/` character as a separator.
2. We use the `map` method to convert the strings into numbers.
3. We define a helper function `gcd` to calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
4. We calculate the product of the numerators and denominators, and then calculate the GCD of the resulting numerator and denominator.
5. We check if the simplified fraction (i.e., the numerator divided by the GCD, and the denominator divided by the GCD) is equal to the original denominator. If it is, we return `true`, indicating that the original expression simplifies to a whole number. Otherwise, we return `false`.