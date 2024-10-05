To solve this problem, we need to first convert the two fractions to their lowest common denominators. Then, we can multiply the two fractions together and determine if the result is a whole number. Here's a step-by-step breakdown:

1. Convert the fractions x and n to their lowest common denominators:
   - For x = a/b, the lowest common denominator is b. So, we don't need to convert it.
   - For n = c/d, the lowest common denominator is d. So, we don't need to convert it.

2. Multiply the two fractions together:
   - The result of multiplying the fractions is (a * c) / (b * d).

3. Determine if the result is a whole number:
   - A fraction is a whole number if the numerator is divisible by the denominator. In this case, if (a * c) is divisible by (b * d), then the result is a whole number, and we return true. Otherwise, we return false.

Here's the code to implement this solution:

```javascript
const simplify = (x, n) => {
  const [a, b] = x.split('/');
  const [c, d] = n.split('/');

  const aMultipliedByC = parseInt(a) * parseInt(c);
  const bMultipliedByD = parseInt(b) * parseInt(d);

  return aMultipliedByC % bMultipliedByD === 0;
};
```

This code first splits the input fractions x and n into their numerator and denominator parts. Then, it multiplies the numerators together and the denominators together. Finally, it checks if the result of multiplying the numerators is divisible by the result of multiplying the denominators. If it is, the function returns true; otherwise, it returns false.

You can use this function to simplify expressions like `simplify("1/5", "5/1")` which will return true, and `simplify("1/6", "2/1")` which will return false.

Note that this solution assumes that the input fractions are always valid and do not have zero as a denominator