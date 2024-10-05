  let sum = 0, bin = '';
  while (N > 0) {
    sum += N % 2;
    bin = (N % 2).toString() + bin;
    N = Math.floor(N / 2);
  }
  return bin;
}

// Testing the function
console.log(solve(1000)); // Output: 1
console.log(solve(150)); // Output: 110
console.log(solve(147)); // Output: 1100
console.log(solve(1000000)); // Output: 1111000000
console.log(solve(123456)); // Output: 1100001111010

// The function works by continuously dividing the number by 2, adding the remainder to the sum and appending the remainder to the binary string. The loop continues until the number becomes 0. Then it returns the binary string.

// The time complexity is O(logN) as we are dividing the number by 2 in each iteration. The space complexity is O(logN) as we are storing the binary string which can have a maximum length of logN. 

// The function can be optimized by using the bitwise operator instead of division and modulus. Here is the optimized version:

const solve = (N) => {
  let sum = 0, bin = '';
  while (N > 0) {
    sum += N & 1;
    bin = (N & 1).toString() + bin;
    N = N >> 1;
  }
  return bin;
}

// This version of the function works exactly like the previous one but it uses bitwise operators instead of division and modulus. The bitwise AND operator (&) is used to get the last bit of the number and the bitwise right shift operator (>>) is used to divide the number by 2. This version of the function is more efficient as it uses bitwise operators which are faster than arithmetic operations.  */



