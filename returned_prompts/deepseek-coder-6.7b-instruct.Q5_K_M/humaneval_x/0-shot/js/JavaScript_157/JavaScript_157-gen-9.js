  // sort the sides of the triangle in ascending order
  const sides = [a, b, c].sort((a, b) => a - b);

  // calculate the square of the hypotenuse and the squares of the other two sides
  const hypotenuseSquare = Math.pow(sides[2], 2);
  const otherTwoSidesSquare = Math.pow(sides[0], 2) + Math.pow(sides[1], 2);

  // return true if the square of the hypotenuse is equal to the sum of the squares of the other two sides
  return hypotenuseSquare === otherTwoSidesSquare;
}


*/



// 