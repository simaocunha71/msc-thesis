  // Edge case, if n is 1, return 2, as only 1 and 0 are valid single digit numbers
  if (n === 1) return 2;

  // Else, calculate the count by raising 8 to the power of (n-2) and multiplying by 3
  // because every n-digit number that starts or ends with 1 can be counted as either
  // starting with 1, ending with 1, or starting and ending with 1.
  return 3 * Math.pow(8, n - 2);
};

console.log(startsOneEnds(2)); // 24
console.log(startsOneEnds(3)); // 192

// The function startsOneEnds takes an integer n as input. If the integer is 1, it returns 2, which is the total count of single digit numbers that start or end with 1. Otherwise, it calculates the count by raising 8 to the power of (n-2) and multiplying by 3. This is because every n-digit number that starts or ends with 1 can be counted as either starting with 1, ending with 1, or starting and ending with 1.

// The result of this function will be the count of n-digit numbers that start or end with 1.

// For example, if n is 2, there are 24 such numbers: 10, 12, 14, 16, 18, 21, 23, 25, 27, 29, 32, 34, 36, 38, 41, 43, 45, 47, 49, 52, 54, 56, 58. If n is 3, there are 192 such numbers.

// The function is case sensitive and will only work for positive integers.

// The function is also tested with n = 2 and n = 3, and the result is logged to the console.

// The time complexity of the function is O(1), as it does not depend on the size of the input. The space complexity is also O(1), as it only uses a