Here's how you might do it in JavaScript:

```javascript
const iscube = (a) => {
  if (a === 0) return true;
  let sqrt = Math.abs(Math.floor(Math.pow(a, 1/3)));
  return sqrt * sqrt * sqrt === a;
}
```

In this solution, we first check if the input is 0, because 0 is a cube of some number (0), and we return true in that case. Then we calculate the cubic root of the absolute value of the input, and round it down to the nearest integer. We check if the cube of this integer is equal to the input, and return true if it is, false otherwise.