```
if (a + b > c && a + c > b && b + c > a) {
  const s = (a + b + c) / 2;
  const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  return Number(area.toFixed(2));
} else {
  return -1;
}
```


Explanation:
The function first checks if the three sides form a valid triangle by verifying the triangle inequality theorem. If the sum of any two sides is greater than the third side, then it's a valid triangle. If not, the function returns -1.

If the triangle is valid, the function calculates the semi-perimeter 's' using the formula (a + b + c) / 2. Then it calculates the area using Heron's formula: √(s * (s - a) * (s - b) * (s - c)). Finally, it rounds the area to 2 decimal points using the toFixed() method and converts it to a number using the Number() constructor. If the area is not a valid number, it will return NaN. To avoid this, we can use the Number() constructor to convert the result to a number before returning it.