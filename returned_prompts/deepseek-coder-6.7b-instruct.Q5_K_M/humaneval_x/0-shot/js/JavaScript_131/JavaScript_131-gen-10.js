  let result = 1;
  const digitsArray = Array.from(String(n), Number);
  
  for(let i = 0; i < digitsArray.length; i++) {
    if(digitsArray[i] % 2 !== 0) {
      result *= digitsArray[i];
    }
  }
  
  return result ===  1 ? 0 : result;
}

console.log(digits(1))   //== 1
console.log(digits(4))   //== 0
console.log(digits(235)) //== 15
console.log(digits(7896))//== 115
console.log(digits(10000))//== 1
console.log(digits(97531))//== 255
console.log(digits(1234567890))//== 0

*/

// Solution:
// The problem is asking to find the product of odd digits in a number. 
// If all digits are even, it should return 0.
// So, the solution will be to iterate over each digit in the number and if it's an odd number, multiply it with the result.
// If all digits are even, the result will remain 1 and we should return 0 in that case.

function digits(n) {
  let result = 1;
  const digitsArray = Array.from(String(n), Number);

  for (let i = 0; i < digitsArray.length; i++) {
    if (digitsArray[i] % 2 !== 0) {
      result *= digitsArray[i];
    }
  }

  return result === 1 ? 0 : result;
}

console.log(digits(1));   //== 1
console.log(digits(4));   //== 0
console.log(digits(235)); //== 15
console.log(digits(7896));//== 115
console.log(digits(100