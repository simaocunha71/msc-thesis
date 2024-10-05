  let result = 1;
  for (let i = n; i > 0; i--) {
    result *= i * specialFactorial(i - 1);
  }
  return result;
}
// Note: This function is not correct. It should return the result of the calculation
//       not the recursive call. This is a recursive function that does not stop,
//       it will cause a stack overflow.
// The correct solution is:
const specialFactorial = (n) => {
  let result = 1;
  for (let i = n; i > 0; i--) {
    result *= i * Math.factorial(i - 1);
  }
  return result;
}  // or
const specialFactorial = (n) => {
  let result = 1;
  for (let i = n; i > 1; i--) {
    result *= i * Math.factorial(i - 1);
  }
  return result;
}
// This solution is using the built-in Math.factorial function
// or it's using the formula for the factorial of a number
// This solution will not work for large numbers because the factorial of a number grows very fast
// and will cause an overflow error.  // 
// A more correct solution would be to use a loop to calculate the factorial
// or to use a library that supports large numbers.