The solution to this problem involves calculating the semi-perimeter of the triangle and then using Heron's formula to calculate the area. However, before calculating the area, we need to check if the three sides form a valid triangle.

Here is the solution:

```javascript
const triangleArea = (a, b, c) => {
  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1; // if the sides do not form a valid triangle
  }
  const s = (a + b + c) / 2; // semi-perimeter
  const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  return Math.round(area * 100) / 100; // round to 2 decimal points
};
```

This function first checks if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If they do not form a valid triangle, the function returns -1.

If the sides do form a valid triangle, the function calculates the semi-perimeter and then uses Heron's formula to calculate the area of the triangle. The area is then rounded to 2 decimal points and returned.

For example, calling `triangleArea(3, 4, 5)` would return `6.00`, and calling `triangleArea(1, 2, 10)` would return `-1`.