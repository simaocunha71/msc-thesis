  return a * a + b * b === c * c || a * a + c * c === b * b || c * c + b * b === a * a;
}
// or
const rightAngleTriangle = (a, b, c) => {
  if (a * a + b * b === c * c || a * a + c * c === b * b || c * c + b * b === a * a) {
    return true;
  }
  return false;
}
// or
const rightAngleTriangle = (a, b, c) => {
  return (Math.sqrt(a * a + b * b) === c || Math.sqrt(a * a + c * c) === b || Math.sqrt(c * c + b * b) === a);
}
// or
const rightAngleTriangle = (a, b, c) => {
  const sides = [a, b, c];
  sides.sort((a, b) => a - b);
  return sides[0] * sides[0] + sides[1] * sides[1] === sides[2] * sides[2];
}
// or
const rightAngleTriangle = (a, b, c) => {
  return Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2)) === c || Math.sqrt(Math.pow(a, 2) + Math.pow(c, 2)) === b || Math.sqrt(Math.pow(c, 2) + Math.pow(b, 2)) === a;
}
// or
const rightAngleTriangle = (a, b, c) => {
  return (Math.sqrt(a * a + b * b) === c || Math.sqrt(a * a + c * c) === b || Math.sqrt(c * c + b * b) === a) ? true : false;
}
// or
const rightAngleTriangle = (a, b, c) => {
  var ab = a * a + b * b;
  var bc = b * b + c * c;
  var ca = c * c + a * a;
  return ab === c * c || bc === a * a || ca === b * b;
}
// or
const rightAngleTriangle = (a, b, c) => {
  return (Math.pow(a, 2) + Math.pow(b, 2) === Math.pow(c, 2) || Math.pow(a, 2) + Math