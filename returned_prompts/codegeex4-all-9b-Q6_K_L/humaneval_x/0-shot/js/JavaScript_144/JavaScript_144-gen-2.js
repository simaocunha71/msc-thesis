To simplify the expression `x * n`, we need to check if the product of the numerators and denominators is a whole number. Here's how we can implement the `simplify` function in JavaScript:

```javascript
const simplify = (x, n) => {
  // Split the fractions into numerator and denominator
  const [xNum, xDen] = x.split('/');
  const [nNum, nDen] = n.split('/');

  // Convert the string representations to numbers
  const num = Number(xNum) * Number(nNum);
  const den = Number(xDen) * Number(nDen);

  // Check if the product of the numerators and denominators is a whole number
  return Number.isInteger(num / den);
};

// Test cases
console.log(simplify("1/5", "5/1")); // true
console.log(simplify("1/6", "2/1")); // false
console.log(simplify("7/10", "10/2")); // false
```

This function splits the fractions into numerators and denominators, multiplies them together, and checks if the result is a whole number by using `Number.isInteger()`.