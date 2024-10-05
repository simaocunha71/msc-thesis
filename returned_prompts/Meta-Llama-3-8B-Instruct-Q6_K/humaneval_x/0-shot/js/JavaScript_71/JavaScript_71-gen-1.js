```javascript
const triangleArea = (a, b, c) => {
  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }
  const s = (a + b + c) / 2;
  const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  return Math.round(area * 100) / 100;
};
```
Here is the explanation of the code:

1. The function takes three arguments `a`, `b`, `c` which are the lengths of the three sides of the triangle.
2. First, we check if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If not, we return -1.
3. If the three sides form a valid triangle, we calculate the semi-perimeter `s` using the formula `(a + b + c) / 2`.
4. Then, we calculate the area of the triangle using Heron's formula `Math.sqrt(s * (s - a) * (s - b) * (s - c))`.
5. Finally, we round the area to 2 decimal points using `Math.round(area * 100) / 100` and return it.

Note: The code uses the `Math.round()` function to round the area to 2 decimal points. This function rounds the number to the nearest integer, so we multiply the area by 100 to shift the decimal point to the right, round it, and then divide by 100 to shift the decimal point back to the left. This ensures that the area is rounded to 2 decimal points.