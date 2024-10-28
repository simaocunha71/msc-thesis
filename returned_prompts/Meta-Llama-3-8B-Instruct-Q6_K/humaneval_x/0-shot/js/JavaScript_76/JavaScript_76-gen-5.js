Here is the solution using JavaScript:

```javascript
const isSimplePower = (x, n) => {
  if (x < 1) return false;
  let base = Math.pow(n, Math.floor(Math.log(x) / Math.log(n)));
  return base === n ** Math.floor(Math.log(x) / Math.log(n));
};
```

This function first checks if the number x is less than 1. If it is, the function immediately returns false because a simple power of n must be greater than or equal to 1.

Next, the function calculates the base of the power by taking the nth root of x and rounding it down to the nearest integer using the Math.floor function.

Finally, the function checks if the calculated base is equal to the nth power of the calculated base. If it is, the function returns true, indicating that x is a simple power of n. If not, the function returns false.