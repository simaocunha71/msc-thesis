```
  const a2 = a * a;
  const b2 = b * b;
  const c2 = c * c;
  
  if (a2 + b2 === c2 || a2 + c2 === b2 || b2 + c2 === a2) {
    return true;
  }
  return false;
```


Explanation:
This function checks if the three sides of a triangle form a right-angled triangle. It does this by using the Pythagorean theorem, which states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.

The function calculates the squares of the three sides and checks if any of the following conditions are true:
- a^2 + b^2 = c^2 (one side is the hypotenuse)
- a^2 + c^2 = b^2 (one side is the hypotenuse)
- b^2 + c^2 = a^2 (one side is the hypotenuse)

If any of these conditions are true, the function returns true, indicating that the triangle is a right-angled triangle. Otherwise, it returns false.