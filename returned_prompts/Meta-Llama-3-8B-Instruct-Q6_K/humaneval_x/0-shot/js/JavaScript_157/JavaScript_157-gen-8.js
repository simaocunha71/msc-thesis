```
  return a * a + b * b === c * c || a * a + c * c === b * b || b * b + c * c === a * a;
```


This code checks if the sum of the squares of two sides of the triangle is equal to the square of the third side. If this condition is met for any two sides, then the triangle is a right-angled triangle. This is a well-known property of right-angled triangles, known as the Pythagorean theorem.

The condition `a * a + b * b === c * c` checks if the square of the first side and the square of the second side is equal to the square of the third side. If this condition is true, then the triangle is a right-angled triangle. The same condition is checked for the other two combinations of sides, `a * a + c * c === b * b` and `b * b + c * c === a * a`.

If any of these conditions are true, the function returns `true`, indicating that the three sides form a right-angled triangle. If none of the conditions are true, the function returns `false`, indicating that the three sides do not form a right-angled triangle.