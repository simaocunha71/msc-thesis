/*Given length of a side and high return area for a triangle.
  >>> triangleArea(5, 3)
  7.5
  */
const triangleArea = (a, h) => {
  const hsq = Math.sqrt((h * h)); // square h
  const s1 = Math.trunc(Math.abs(0.5 * a / Math.sin(Math.PI)));
  const s2 = Math.trunc(Math.abs(0.5 * a / Math.cos(Math.PI / 4)))
  return ((s1 + s2) * hsq);
};

console.log(triangleArea(10, 3));