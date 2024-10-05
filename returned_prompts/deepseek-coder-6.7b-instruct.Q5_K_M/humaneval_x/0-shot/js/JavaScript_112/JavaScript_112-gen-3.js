  let str = '';
  for(let i=0; i<s.length; i++) {
    if(!c.includes(s[i])) {
      str += s[i];
    }
  }
  let rev = str.split('').reverse().join('');
  let res = (str == rev) ? true : false;
  return [str,res];
}

console.log(reverseDelete('abcde', 'ae')); // ['bcd', false]
console.log(reverseDelete('abcdef', 'b')); // ['acdef', false]
console.log(reverseDelete('abcdedcba', 'ab')); // ['cdedc', true]

*/

/* 
Solution Explanation:
1. I create an empty string str.
2. I iterate over the string s and if the character is not in c, I add it to str.
3. I reverse str and check if it is equal to str. If it is, I return true, else I return false.
4. I return the result string and the result of the check.
*/

/*
Complexity Analysis:
Time Complexity: O(n), where n is the length of the string s.
Reason: I iterate over the string s once.
Space Complexity: O(n), where n is the length of the string s.
Reason: I use an extra space to store the result string.
*/

/*
Test Cases:
console.log(reverseDelete('abcde', 'ae')); // ['bcd', false]
console.log(reverseDelete('abcdef', 'b')); // ['acdef', false]
console.log(reverseDelete('abcdedcba', 'ab')); // ['cdedc', true]
*/

































































































