  let x = Math.round(Math.exp(Math.log(Math.abs(a)) / 3));
  return x * x * x === Math.abs(a);
}

console.log(iscube(1)) // true
console.log(iscube(2)) // false
console.log(iscube(-1)) // true
console.log(iscube(64)) // true
console.log(iscube(0)) // true
console.log(iscube(180)) // false

// Explanation:
// The function iscube calculates the cubic root of the absolute value of the input, rounds it to the nearest whole number,
// and checks if the cube of this rounded value is equal to the absolute value of the input.
// If it is, the function returns true, indicating that the input is a cube of some integer number. If not, it returns false.
// For example, if a is 1, the cubic root of 1 is 1, its cube is 1, and 1 equals 1, so the function returns true.
// If a is 2, the cubic root of 2 is approximately 1.258, rounded to 1, and its cube is 1, but 2 is not equal to 1, so the function returns false.
// The function works for negative numbers by taking the absolute value of the input before calculating the cubic root.
// In JavaScript, Math.exp(Math.log(x) / n) can be used to calculate the nth root of x. Here, Math.log(x) / 3 is used to calculate the cubic root of x.
// The function also works for zero, returning true because 0 is a cube of 0.
// Finally, the function does not work for non-integer numbers. If a is not an integer, the cubic root calculation will not be exact, and the function will return false.
// For example, if a is 180, the cubic root of 180 is approximately 6.22, rounded to 6, and its cube is 216, but 180 is not equal to 216, so the function returns false.
module.exports = iscube;

// Note: This