```
const rightAngleTriangle = (a, b, c) => {
  // Pythagorean theorem
  const a2 = a ** 2;
  const b2 = b ** 2;
  const c2 = c ** 2;
  // Check if any two sides can be the hypotenuse
  if (a2 + b2 === c2 || a2 + c2 === b2 || b2 + c2 === a2) {
    return true;
  }
  // If no combination of sides can be the hypotenuse, return false
  return false;
};
```