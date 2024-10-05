To solve this problem, we need to convert the fractions to floating-point numbers and check if their product is a whole number. Here's how we can implement the `simplify` function:

```javascript
const simplify = (x, n) => {
  // Split the fractions into their numerator and denominator
  const [numeratorX, denominatorX] = x.split('/');
  const [numeratorN, denominatorN] = n.split('/');

  // Convert the fractions to floating-point numbers
  const numX = parseFloat(numeratorX) / parseFloat(denominatorX);
  const numN = parseFloat(numeratorN) / parseFloat(denominatorN);

  // Check if their product is a whole number
  return Number.isInteger(numX * numN);
};
```

Let's test the function with the provided examples:

```javascript
console.log(simplify("1/5", "5/1")); // true
console.log(simplify("1/6", "2/1")); // false
console.log(simplify("7/10", "10/2")); // false
```

The output should be:

```
true
false
false
```

This solution splits the fractions into their numerator and denominator, converts them to floating-point numbers, and then checks if their product is a whole number using the `Number.isInteger` function.