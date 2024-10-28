  let newS = '';
  for(let i=0; i<s.length; i++){
    if(!c.includes(s[i])){
      newS += s[i];
    }
  }
  
  let revS = newS.split('').reverse().join('');
  
  return [revS, revS === newS];
}
*/

/* 
This solution works by initializing a new string, newS, to empty string. Then it iterates through each character of string s. If the character is not included in the string c, it adds that character to newS. 

Then it reverses newS and compares it with s. If they are equal, it means that the string is palindrome after deletion of characters in c, so it returns a tuple with reversed string and true. If they are not equal, it returns a tuple with reversed string and false.
*/

// Test cases
console.log(reverseDelete("abcde", "ae")); //  should return  ('e', false)
console.log(reverseDelete("abcdef", "b")); //  should return  ('f', false)
console.log(reverseDelete("abcdedcba", "ab")); //  should return  ('a', true)

```

## ➔ Solution:

This solution works by initializing a new string, newS, to empty string. Then it iterates through each character of string s. If the character is not included in the string c, it adds that character to newS. 

Then it reverses newS and compares it with s. If they are equal, it means that the string is palindrome after deletion of characters in c, so it returns a tuple with reversed string and true. If they are not equal, it returns a tuple with reversed string and false.

```javascript
const reverseDelete = (s, c) => {
  let newS = '';
  for(let i=0; i<s.length; i++){
    if(!c.includes(s[i])){
      newS += s[i];
    }
  }
  let revS = newS.split('').reverse().join('');
