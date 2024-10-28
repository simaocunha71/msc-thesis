You can solve this problem using the Pythagorean theorem. According to the theorem, in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. Here is how you can implement this in JavaScript:

```javascript
const rightAngleTriangle = (a, b, c) => {
  let sides = [a, b, c];
  sides.sort((a, b) => a - b);
  return sides[0]**2 + sides[1]**2 === sides[2]**2;
};
```

In this code, we first sort the sides of the triangle in ascending order. The reason for this is that we know that the hypotenuse will be the longest side, so after sorting the sides, the third element in the array (`sides[2]`) will be the hypotenuse.

We then return `true` if the sum of the squares of the two smaller sides is equal to the square of the largest side (the hypotenuse), and `false` otherwise.