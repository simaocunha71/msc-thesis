const triangleArea = (a, b, c) => {
  if (a + b < c || b + c < a || c + a < b) {
    return -1;
  }
  const semiPerimeter = (a + b + c) / 2;
  const area = Math.sqrt(semiPerimeter * (semiPerimeter - a) * (semiPerimeter - b) * (semiPerimeter - c));
  return area.toFixed(2);
};
