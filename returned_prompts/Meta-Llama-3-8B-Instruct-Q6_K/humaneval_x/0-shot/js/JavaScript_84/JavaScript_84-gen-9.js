  let sum = 0;
  let binary = N.toString(2);
  for (let i = 0; i < binary.length; i++) {
    if (binary[i] === '1') {
      sum += 1;
    }
  }
  return sum.toString();
};
// Test cases
console.log(solve(1000)); // Output: "1"
console.log(solve(150)); // Output: "6"
console.log(solve(147)); // Output: "12"
console.log(solve(123)); // Output: "3"
console.log(solve(10000)); // Output: "10"*/

function solve(N) {
  let binary = N.toString(2);
  let sum = 0;
  for (let i = 0; i < binary.length; i++) {
    if (binary[i] === '1') {
      sum += 1;
    }
  }
  return sum.toString();
}
// Test cases
console.log(solve(1000)); // Output: "1"
console.log(solve(150)); // Output: "6"
console.log(solve(147)); // Output: "12"
console.log(solve(123)); // Output: "3"
console.log(solve(10000)); // Output: "10"*/


// Improved solution
function solve(N) {
  return N.toString(2).split('').filter(c => c === '1').length.toString();
}
// Test cases
console.log(solve(1000)); // Output: "1"
console.log(solve(150)); // Output: "6"
console.log(solve(147)); // Output: "12"
console.log(solve(123)); // Output: "3"
console.log(solve(10000)); // Output: "10"*/



// Solution using regex
function solve(N) {
  return (N.toString(2).match(/1/g) || []).length.toString();
}
// Test cases
console.log(solve(1000)); // Output: "1"
console.log(solve(150)); // Output: "6"
console.log(solve(147)); // Output: "12"
console.log(solve(123)); // Output: "3"
console.log(solve(10000)); // Output: "10"*/



// Solution using map and reduce
function solve(N) {
  return parseInt(N.toString(2).split('').map(c => c === '1' ? 1 : 0).reduce