  let count = 0;
  for(let i = 0; i < s.length; i += 2) {
    if(['A', 'E', 'I', 'O', 'U'].indexOf(s[i]) !== -1) {
      count++;
    }
  }
  return count;
}
*/

// Answer
const countUpper = (s) => {
  let count = 0;
  for(let i = 0; i < s.length; i += 2) {
    if(['A', 'E', 'I', 'O', 'U'].includes(s[i])) {
      count++;
    }
  }
  return count;
}

console.log(countUpper('aBCdEf')); // 1
console.log(countUpper('abcdefg')); // 0
console.log(countUpper('dBBE')); // 0


// Solution Explanation:
// The function countUpper loops through the input string s, checking every two characters (the even indices) to see if they are uppercase vowels. If they are, it increments the count variable. It then returns the count.
// The function uses the array method "includes()" instead of "indexOf()" to simplify the code. 
// The function also uses an array of uppercase vowels to simplify the code and make it more readable.
// The function assumes that the input string s only contains uppercase and lowercase letters. If the input string contains other characters, the function may not work correctly.

// Refactoring:
// We can refactor the code to use the Array.from() method to loop over the string, checking each character at its corresponding index. This will simplify the code and make it more readable.

const countUpperRefactored = (s) => {
  return Array.from(s).reduce((count, char, index) => 
    index % 2 === 0 && ['A', 'E', 'I', 'O', 'U'].includes(char) ? count + 1 : count, 0);
}

console.log(countUpperRefactored('aBCdEf')); // 1
console.log(countUpperRefactored('abcdefg