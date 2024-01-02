/*Given length of a side and high return area for a triangle.
  >>> triangleArea(5, 3)
  7.5
  */
const triangleArea = (a, h) => {
  const AREA_SQUARED = 0.5 * h * ((a + 1) ** 2);
  return Math.round(AREA_SQUARED);
};
console.log(triangleArea(3, 4));
