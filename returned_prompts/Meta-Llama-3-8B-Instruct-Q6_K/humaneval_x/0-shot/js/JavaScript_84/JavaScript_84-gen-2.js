let sum = 0;
let binary = N.toString(2);
for (let i = 0; i < binary.length; i++) {
  sum += parseInt(binary[i]);
}
return sum.toString();
};
console.log(solve(1000)); // "1"
console.log(solve(150)); // "110"
console.log(solve(147)); // "1100"  // 1 + 4 + 7 = 12
console.log(solve(101)); // "2" // 1 + 0 + 1 = 2
console.log(solve(1001)); // "1" // 1 + 0 + 0 + 1 = 2
console.log(solve(2)); // "2" // 2 = 2
console.log(solve(3)); // "2" // 1 + 1 + 1 = 3
console.log(solve(9)); // "2" // 1 + 0 + 0 + 0 + 1 = 2
console.log(solve(10)); // "2" // 1 + 0 = 1

// the binary representation of 10 is 1010
// sum of digits 1+0+1+0 = 2
// the binary representation of 10 is 1010
// sum of digits 1+0+1+0 = 2
// the binary representation of 10 is 1010
// sum of digits 1+0+1+0 = 2

// the binary representation of 9 is 1001
// sum of digits 1+0+0+1 = 2
// the binary representation of 9 is 1001
// sum of digits 1+0+0+1 = 2
// the binary representation of 9 is 1001
// sum of digits 1+0+0+1 = 2

// the binary representation of 3 is 11
// sum of digits 1+1 = 2
// the binary representation of 3 is 11
// sum of digits 1+1 = 2
// the binary representation of 3 is 11
// sum of digits 1+1 = 2

// the binary representation of 2 is 10
// sum of digits 1+0 = 1
// the binary representation of 2 is 10
// sum of digits