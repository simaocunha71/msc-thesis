  let unitDigitA = Math.abs(a) % 10;
  let unitDigitB = Math.abs(b) % 10;
  return unitDigitA * unitDigitB;
}

console.log(multiply(148, 412));  // 16
console.log(multiply(19, 28));     // 72
console.log(multiply(2020, 1851)); // 0
console.log(multiply(14,-15));     // 20

// 1. extract the unit digit of 'a' and 'b' using the modulo 10 operation
// 2. return the product of these two unit digits

// Math.abs is used to handle negative numbers by converting them to positive.
// This is because the unit digit of a negative number is the same as the unit digit of its positive counterpart.
// e.g. unit digit of -14 is the same as unit digit of 14.

// This way we are only dealing with positive numbers and avoid dealing with the negative unit digit case.

// % is the modulo operator which gives the remainder of a division.
// e.g. 14 % 10 = 4, because 14 divided by 10 is 1 remainder 4.
// This is how we get the unit digit of a number.

// * is the multiplication operator.
// e.g. 4 * 5 = 20.
// This is how we compute the product of the unit digits.

// => is the arrow function syntax.
// It is a shorter syntax for function expressions.
// e.g. let multiply = function(a, b) { ... }
// can be written as let multiply = (a, b) => { ... }.
// In this case, it is used because the function expression takes two arguments 'a' and 'b' and returns the product of their unit digits.

// In the function, Math.abs is used to make sure that the function can handle negative numbers.
// Math.abs returns the absolute value of a number, which is the value without the negative sign.
// For negative