```
function triangleArea(a, b, c) {
  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }
  const s = (a + b + c) / 2;
  const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  return Math.round(area * 100) / 100;
}
```


Explanation:
The function first checks if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If not, it returns -1.

If the three sides form a valid triangle, it calculates the area using Heron's formula. The formula is: `sqrt(s * (s - a) * (s - b) * (s - c))`, where `s` is the semi-perimeter of the triangle.

Finally, it rounds the area to 2 decimal points using `Math.round(area * 100) / 100`. The `Math.round` function rounds the area to the nearest integer, and then the `/ 100` operation divides the result by 100 to get the area rounded to 2 decimal points.