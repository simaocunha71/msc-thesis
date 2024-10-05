  var c = Math.round(Math.pow(Math.abs(a), (1/3)));
  return c * c * c === a;
}  // This function works by first taking the cube root of the number and rounding it to the nearest integer.
// Then it checks if the cube of that integer is equal to the original number. If it is, the function returns true. Otherwise, it returns false.