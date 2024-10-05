  if (a * a + b * b === c * c || a * a + c * c === b * b || b * b + c * c === a * a) {
    return true;
  }
  return false;
}
// or
const rightAngleTriangle = (a, b, c) => {
  let sides = [a, b, c];
  sides.sort((a, b) => a - b);
  return sides[0] * sides[0] + sides[1] * sides[1] === sides[2] * sides[2];
}
// or
const rightAngleTriangle = (a, b, c) => {
  let sides = [a, b, c];
  sides.sort((a, b) => a - b);
  return sides[0] * sides[0] + sides[1] * sides[1] === sides[2] * sides[2] || sides[0] * sides[0] + sides[2] * sides[2] === sides[1] * sides[1] || sides[1] * sides[1] + sides[2] * sides[2] === sides[0] * sides[0];
}
// or
const rightAngleTriangle = (a, b, c) => {
  return (a * a + b * b === c * c) || (a * a + c * c === b * b) || (b * b + c * c === a * a);
}