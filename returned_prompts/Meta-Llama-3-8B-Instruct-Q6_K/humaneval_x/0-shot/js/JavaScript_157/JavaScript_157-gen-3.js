```
const rightAngleTriangle = (a, b, c) => {
  // Pythagorean theorem: a^2 + b^2 = c^2 for a right-angled triangle
  return (a * a + b * b === c * c);
};
```
Explanation:
The problem is asking to determine if three given side lengths form a right-angled triangle. A right-angled triangle is defined by the Pythagorean theorem: a^2 + b^2 = c^2, where a and b are the lengths of the shorter sides and c is the length of the hypotenuse (the longest side).

In the given code, the function `rightAngleTriangle` takes three arguments `a`, `b`, and `c` representing the side lengths. It returns a boolean value indicating whether the three sides form a right-angled triangle or not.

The condition `a * a + b * b === c * c` checks if the Pythagorean theorem is satisfied. If the sum of the squares of the shorter sides equals the square of the longest side, the function returns `true`, indicating that the three sides form a right-angled triangle. Otherwise, it returns `false`.