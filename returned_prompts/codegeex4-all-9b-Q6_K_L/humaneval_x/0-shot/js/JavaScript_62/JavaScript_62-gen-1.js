Here is the solution in JavaScript:

```javascript
const derivative = (xs) => {
  return xs.slice(1).map((x, i) => i + 1 * x);
};

console.log(derivative([3, 1, 2, 4, 5])); // [1, 4, 12, 20]
console.log(derivative([1, 2, 3])); // [2, 6]
```

This function creates a new array that contains all elements from the original array except for the first one. Then it maps over this new array and multiplies each element by its index + 1. This gives us the derivative of the polynomial.