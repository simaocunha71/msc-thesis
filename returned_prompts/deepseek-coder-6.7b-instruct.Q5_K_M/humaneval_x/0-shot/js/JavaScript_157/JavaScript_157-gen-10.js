  //First sort the sides of the triangle in ascending order
  const sortedSides = [a, b, c].sort((a, b) => a - b);

  //Then check if the square of the largest side is equal to the sum of the squares of the other two sides
  return Math.pow(sortedSides[2], 2) === Math.pow(sortedSides[0], 2) + Math.pow(sortedSides[1], 2);
}

// Test cases:
console.log(rightAngleTriangle(3, 4, 5));  // true
console.log(rightAngleTriangle(1, 2, 3));  // false
console.log(rightAngleTriangle(5, 12, 13));  // true
console.log(rightAngleTriangle(6, 8, 10));  // true
console.log(rightAngleTriangle(7, 24, 25));  // true
console.log(rightAngleTriangle(3, 6, 8));  // false
```

The function works by first sorting the three input lengths in ascending order. This allows it to compare the squares of the largest side (the hypotenuse of the right-angled triangle) to the sum of the squares of the other two sides (the legs of the triangle). If these two values are equal, then the three sides form a right-angled triangle, and the function returns true. Otherwise, it returns false.

Here, we are using the Pythagorean Theorem, a fundamental theorem in the field of mathematics, which states that in a right-angled triangle, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides.

In JavaScript, we can use the `Math.pow()` function to square a number, and the `Array.prototype.sort()` method to sort the three lengths in ascending order.

Note: The sorting function is not strictly necessary for this problem, but it makes the code easier to understand and less error-prone, as it ensures that the sides are ordered from smallest to largest.

The time complexity of this function is O(1), because