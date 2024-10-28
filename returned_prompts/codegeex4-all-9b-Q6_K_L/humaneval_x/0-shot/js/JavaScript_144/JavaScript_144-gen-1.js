The problem requires us to determine if the product of two fractions, x and n, is a whole number. To simplify the problem, we can convert the fractions into decimal representations and then check if the result is an integer.

Here is a possible solution in JavaScript:

```javascript
const simplify = (x, n) => {
  const [numeratorX, denominatorX] = x.split('/').map(Number);
  const [numeratorN, denominatorN] = n.split('/').map(Number);

  const productNumerator = numeratorX * numeratorN;
  const productDenominator = denominatorX * denominatorN;

  return Number.isInteger(productNumerator / productDenominator);
};

console.log(simplify("1/5", "5/1")); // true
console.log(simplify("1/6", "2/1")); // false
console.log(simplify("7/10", "10/2")); // false
```

In the above code, we first split the input strings x and n into their numerator and denominator parts. We then calculate the product of the numerators and the product of the denominators. Finally, we use the `Number.isInteger` function to check if the result of the division is an integer.