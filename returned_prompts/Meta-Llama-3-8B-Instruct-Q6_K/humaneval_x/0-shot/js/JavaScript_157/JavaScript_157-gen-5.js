```
  if (a >= b && a >= c) {
    let side1 = a;
    let side2 = b;
    let side3 = c;
  } else if (b >= a && b >= c) {
    let side1 = b;
    let side2 = a;
    let side3 = c;
  } else {
    let side1 = c;
    let side2 = a;
    let side3 = b;
  }

  if (side1 ** 2 === side2 ** 2 + side3 ** 2) {
    return true;
  } else {
    return false;
  }
};
```


The function `rightAngleTriangle` takes three arguments `a`, `b`, and `c` which are the lengths of the three sides of a triangle. It returns `true` if the three sides form a right-angled triangle, and `false` otherwise.

The function first sorts the three sides in ascending order to ensure that the longest side is always `side1`, the middle side is `side2`, and the shortest side is `side3`.

Then it checks if the square of the longest side (`side1`) is equal to the sum of the squares of the other two sides (`side2` and `side3`). This is the Pythagorean theorem, which states that in a right-angled triangle, the square of the length of the hypotenuse (the longest side) is equal to the sum of the squares of the lengths of the other two sides.

If this condition is true, the function returns `true`, indicating that the three sides form a right-angled triangle. Otherwise, it returns `false`.