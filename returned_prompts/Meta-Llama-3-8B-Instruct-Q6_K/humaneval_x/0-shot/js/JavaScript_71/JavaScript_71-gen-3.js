```
const triangleArea = (a, b, c) => {
  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }
  const p = (a + b + c) / 2;
  const area = Math.sqrt(p * (p - a) * (p - b) * (p - c));
  return Math.round(area * 100) / 100;
};
```


Explanation:
The function first checks if the three sides can form a valid triangle by checking if the sum of any two sides is greater than the third side. If not, it returns -1.

If the sides form a valid triangle, it calculates the area using Heron's formula. This formula is based on the fact that the area of a triangle is equal to the square root of the product of the three sides' lengths and the semi-perimeter (the sum of the three sides divided by 2).

Finally, it rounds the calculated area to 2 decimal points using the `Math.round` function. The `* 100` is used to multiply the area by 100 before rounding, and then dividing by 100 to get the correct decimal places. This is a common trick to round a number to a specific number of decimal places in JavaScript.