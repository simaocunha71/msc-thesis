Here is the solution using a dictionary to count the frequency of each character in both strings:
```javascript
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  const charCount0 = {};
  const charCount1 = {};
  
  for (let char of s0) {
    charCount0[char] = (charCount0[char] || 0) + 1;
  }
  
  for (let char of s1) {
    charCount1[char] = (charCount1[char] || 0) + 1;
  }
  
  for (const char in charCount0) {
    if (charCount0[char] !== charCount1[char]) return false;
  }
  
  return true;
};
```
This function first checks if the lengths of the two strings are equal. If not, it returns `false` because the strings cannot have the same characters. Then, it creates two dictionaries to count the frequency of each character in both strings. Finally, it iterates over the characters in the first dictionary and checks if the frequency of each character is the same in both dictionaries. If it finds a character with different frequencies, it returns `false`. If it doesn't find any such character, it returns `true`.