Here's one way you can implement the `simplify` function in JavaScript:

```javascript
const simplify = (x, n) => {
  const [numX, denX] = x.split('/').map(Number);
  const [numN, denN] = n.split('/').map(Number);
  const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);
  const commonDenominator = denX * denN / gcd(denX, denN);
  const num = numX * (commonDenominator / denX) + numN * (commonDenominator / denN);
  return num % 1 === 0;
}
```

This function first splits the input strings `x` and `n` by `/` to extract the numerators and denominators, then converts them to numbers.

Next, it calculates the greatest common divisor (gcd) of the denominators using the `gcd` function.

Then, it calculates the common denominator of the fractions by dividing the product of the denominators by their gcd.

After that, it calculates the numerator of the resulting fraction by adding the numerators of the fractions, each multiplied by the ratio of the common denominator to its respective denominator.

Finally, it returns true if the numerator of the resulting fraction is a whole number (i.e., has a remainder of 0 when divided by 1), and false otherwise.