  // First, sort the sides in ascending order.
  const sortedSides = [a, b, c].sort((a, b) => a - b);

  // Then, check if the square of the largest side is equal to the sum of the squares of the other two sides.
  // This is a special property of right-angled triangles where a^2 + b^2 = c^2.
  return Math.pow(sortedSides[2], 2) === Math.pow(sortedSides[0], 2) + Math.pow(sortedSides[1], 2);
};

console.log(rightAngleTriangle(3, 4, 5));  // Expected output: true
console.log(rightAngleTriangle(1, 2, 3));  // Expected output: false

*/


// ----------------------------------------



// ----------------------------------------


/*
