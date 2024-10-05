```
const rightAngleTriangle = (a, b, c) => {
  // Pythagorean theorem: a^2 + b^2 = c^2
  return Math.sqrt(a * a + b * b) === c || a * a + b * b === c * c;
};
```


Explanation:

*   We use the Pythagorean theorem to check if the three sides form a right-angled triangle. The theorem states that for a right-angled triangle, the square of the length of the hypotenuse (c) is equal to the sum of the squares of the lengths of the other two sides (a and b).
*   We use the `Math.sqrt` function to calculate the square root of the sum of the squares of `a` and `b`. If this value is equal to `c`, then the three sides form a right-angled triangle.
*   Alternatively, we can also check if the sum of the squares of `a` and `b` is equal to the square of `c`. If this condition is met, then the three sides also form a right-angled triangle.
*   The `||` operator is used to check both conditions, and the function returns `true` if either condition is met, and `false` otherwise.

You can test the function with different inputs to verify its correctness. For example, `rightAngleTriangle(3, 4, 5)` should return `true`, and `rightAngleTriangle(1, 2, 3)` should return `false`.