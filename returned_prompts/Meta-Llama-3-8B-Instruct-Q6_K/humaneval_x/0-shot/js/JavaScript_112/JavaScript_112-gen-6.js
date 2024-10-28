/*Task
  We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
  then check if the result string is palindrome.
  A string is called palindrome if it reads the same backward as forward.
  You should return a tuple containing the result string and true/false for the check.
  Example
  For s = "abcde", c = "ae", the result should be ('bcd',false)
  For s = "abcdef", c = "b"  the result should be ('acdef',false)
  For s = "abcdedcba", c = "ab", the result should be ('cdedc',true)
  */
const reverseDelete = (s, c) => {
  // create a new string without characters from c
  let result = s.split('').filter(x => !c.includes(x)).join('');
  
  // check if the result string is palindrome
  let isPalindrome = result === result.split('').reverse().join('');
  
  return [result, isPalindrome];
};*/



// Example usage:
console.log(reverseDelete("abcde", "ae")); // Output: ['bcd', false]
console.log(reverseDelete("abcdef", "b")); // Output: ['acdef', false]
console.log(reverseDelete("abcdedcba", "ab")); // Output: ['cdedc', true]
console.log(reverseDelete("a", "a")); // Output: ['', false] */






