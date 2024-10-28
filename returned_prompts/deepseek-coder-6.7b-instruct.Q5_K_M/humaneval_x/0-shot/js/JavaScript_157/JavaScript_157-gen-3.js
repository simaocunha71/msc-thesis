  // sort the sides in ascending order
  const sorted = [a, b, c].sort((a, b) => a - b);

  // check if the square of the largest side is equal to the sum of the squares of the other two sides
  return Math.pow(sorted[2], 2) === Math.pow(sorted[0], 2) + Math.pow(sorted[1], 2);
}

console.log(rightAngleTriangle(3, 4, 5)); // == true
console.log(rightAngleTriangle(1, 2, 3)); // == false
console.log(rightAngleTriangle(5, 12, 13)); // == true
console.log(rightAngleTriangle(6, 8, 10)); // == true
console.log(rightAngleTriangle(7, 24, 25)); // == true
console.log(rightAngleTriangle(3, 6, 8)); // == false

// This is a very straightforward solution. It first sorts the three numbers in ascending order.
// Then it checks if the square of the largest number (which is the third number in the sorted list) is equal to the sum of the squares of the other two numbers.
// If it is, then the three numbers form a right-angled triangle.
// If it's not, then they don't form a right-angled triangle.

// The reason why this works is that the Pythagorean theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.
// So, if the three numbers form a right-angled triangle, then the square of the largest number (which is the hypotenuse) should be equal to the sum of the squares of the other two numbers.
// If the three numbers don't form a right-angled triangle, then the square of the largest number won't be equal to the sum of the squares of the other two numbers.
// Therefore, by checking if the square of the largest number is equal to the sum of the squares of the other two numbers, we can determine if