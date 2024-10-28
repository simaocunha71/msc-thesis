  let x = Math.round(Math.cbrt(Math.abs(a)));
  return x*x*x === Math.abs(a);
};

console.log(iscube(1)); // true
console.log(iscube(2)); // false
console.log(iscube(-1)); // true
console.log(iscube(64)); // true
console.log(iscube(0)); // true
console.log(iscube(180)); // false

// Math.cbrt(a) returns the cube root of a
// Math.round(x) returns the value of x rounded to the nearest integer.
// Math.abs(a) returns the absolute value of a.

// If the cubed value of x is equal to the absolute value of a then return true else return false.
// This means if a is a perfect cube then the cube of its cubic root will be equal to a.
// For example: cube root of 64 is 4, so 4*4*4 = 64. Hence 64 is a perfect cube.
// Similarly, for -1, cube root is 1, so 1*1*1 = -1, which is not equal to -1. But -1*-1*-1 = 1. Hence -1 is a perfect cube.
// 0 is also a perfect cube as 0*0*0 = 0.
// Hence the function iscube(a) returns true if a is a perfect cube else it returns false.

// This function works by first calculating the cubic root of a in absolute terms using Math.cbrt(a) and then rounding this to the nearest integer using Math.round(x).
// Then it checks if the cubic of this rounded value is equal to the absolute value of a. If it is, then a is a perfect cube and the function returns true. Else, it returns false.

// Note: This function works for positive and negative integers.

// The time complexity of this function is O(1).
// The space complexity of this function is O(1).

// Note: This function uses JavaScript's Math object for its mathematical operations.
// The Math object provides properties and methods for mathematical constants and functions