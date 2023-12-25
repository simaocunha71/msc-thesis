/*
 Given the lengths of the three sides of a triangle. Return true if the three
  sides form a right-angled triangle, false otherwise.
  A right-angled triangle is a triangle in which one angle is right angle or
  90 degree.
  Example:
  rightAngleTriangle(3, 4, 5) == true
  rightAngleTriangle(1, 2, 3) == false
  */
const rightAngleTriangle = (a, b, c) => {
  if (c === undefined || a === undefined || b === undefined) return -1;
  const ab = a > b ? a : b; // get smallest number in the three numbers
  const ac = c > a ? c : a; // get largest number in the three numbers

  const triangle = Math.sqrt(Math.pow(ac, 2) + Math.pow(ab, 2));

  if (triangle < 1 && triangle <= 0) return -1;
  else {
    return triangle === ac || triangle === ab ? 1 : 0;
  }
};
