To solve this problem, we can use Heron's formula to calculate the area of the triangle. This formula is derived from the lengths of the three sides of a triangle.

Here is the step-by-step logic to solve this problem:

1. Check if the three sides can form a valid triangle. A triangle is valid if the sum of any two sides is greater than the third side. If it's not valid, return -1.
2. Calculate the semi-perimeter (s) of the triangle by adding the three sides and dividing by 2.
3. Calculate the area using Heron's formula: area = sqrt(s * (s - a) * (s - b) * (s - c)).
4. Return the area rounded to two decimal points.

Here's the implementation of the above steps:

```javascript
const triangleArea = (a, b, c) => {
  // Step 1: Check if the triangle is valid
  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }

  // Step 2: Calculate the semi-perimeter (s)
  const s = (a + b + c) / 2;

  // Step 3: Calculate the area using Heron's formula
  const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));

  // Step 4: Return the area rounded to two decimal points
  return parseFloat(area.toFixed(2));
};
```

You can use this implementation to calculate the area of a triangle with the given side lengths.

*/

triangleArea(3, 4, 5);  // Returns 6.00
triangleArea(1, 2, 10); // Returns -1









/*
To validate if the three sides can form a valid triangle, we can use the following logic:

If (a + b > c && a + c > b && b + c > a) {
  // The sides can form a valid triangle
} else {
  // The sides cannot form a valid triangle
}

We can simpl