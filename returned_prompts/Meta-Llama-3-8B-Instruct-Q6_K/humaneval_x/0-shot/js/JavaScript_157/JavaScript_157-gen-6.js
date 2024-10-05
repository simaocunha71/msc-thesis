```javascript
const rightAngleTriangle = (a, b, c) => {
  const sides = [a, b, c].sort((a, b) => a - b);
  return sides[0] ** 2 + sides[1] ** 2 === sides[2] ** 2;
};
```
Explanation:
The problem is asking to check if the given three sides can form a right-angled triangle. A right-angled triangle has one angle of 90 degrees, and this can be determined by the Pythagorean theorem: the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides.

In the code, we first sort the sides in ascending order to ensure that `sides[0]` is the smallest side, `sides[1]` is the middle side, and `sides[2]` is the largest side (which is the hypotenuse). Then we check if the square of the hypotenuse (`sides[2]` ** 2`) is equal to the sum of the squares of the other two sides (`sides[0]` ** 2 + `sides[1]` ** 2`). If this condition is true, it means that the three sides can form a right-angled triangle, and we return `true`. Otherwise, we return `false`.