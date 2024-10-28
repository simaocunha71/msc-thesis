```
function triangleArea(a, b, c) {
  // Sort the sides in ascending order
  [a, b, c] = [a, b, c].sort((a, b) => a - b);

  // Check if the sides form a valid triangle
  if (a + b <= c) return -1;

  // Calculate the semi-perimeter
  const s = (a + b + c) / 2;

  // Calculate the area using Heron's formula
  const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));

  // Round the area to 2 decimal points
  return Math.round(area * 100) / 100;
}
```


Explanation:
We first sort the sides in ascending order to make it easier to calculate the semi-perimeter and area. Then, we check if the sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If not, we return -1.

If the sides form a valid triangle, we calculate the semi-perimeter `s` as the sum of the sides divided by 2. Then, we calculate the area using Heron's formula, which is `sqrt(s * (s - a) * (s - b) * (s - c))`.

Finally, we round the area to 2 decimal points using `Math.round(area * 100) / 100`. This is done by multiplying the area by 100, rounding it to the nearest integer using `Math.round`, and then dividing by 100 to get the area rounded to 2 decimal points.