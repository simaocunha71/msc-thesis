You can use the Pythagorean theorem to determine if a triangle is right-angled. The theorem states that in a right triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides. Here's how you can implement the rightAngleTriangle function:

```javascript
const rightAngleTriangle = (a, b, c) => {
  // Ensure that a is the longest side (hypotenuse)
  if (a < b) {
    [a, b] = [b, a];
  }
  if (a < c) {
    [a, c] = [c, a];
  }
  
  // Calculate the squares of the sides
  const aSquared = a * a;
  const bSquared = b * b;
  const cSquared = c * c;
  
  // Check if the square of the longest side is equal to the sum of the squares of the other two sides
  return aSquared === bSquared + cSquared;
};
```

This function first ensures that `a` is the longest side by swapping the values of `a` and `b` or `a` and `c` if necessary. Then it calculates the squares of the sides and checks if the square of the longest side is equal to the sum of the squares of the other two sides. If this condition is met, the function returns `true`, indicating that the triangle is right-angled. Otherwise, it returns `false`.