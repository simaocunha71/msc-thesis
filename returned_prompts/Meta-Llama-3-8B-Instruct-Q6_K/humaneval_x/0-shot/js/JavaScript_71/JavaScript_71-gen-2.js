```
const triangleArea = (a, b, c) => {
  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }
  const s = (a + b + c) / 2;
  const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  return Math.round(area * 100) / 100;
};
``` A solution that works is to first check if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If they don't form a valid triangle, return -1. If they do, calculate the area of the triangle using Heron's formula and return the result rounded to 2 decimal points.

The area of a triangle can be calculated using Heron's formula:
```
area = sqrt(s * (s - a) * (s - b) * (s - c))
```
where `s` is the semi-perimeter of the triangle, which is the sum of the lengths of the sides divided by 2.

To round the result to 2 decimal points, we use the `Math.round` function to round the result to the nearest integer and then divide by 100. This effectively rounds the result to 2 decimal points. We also use the `Math.sqrt` function to calculate the square root of the area.