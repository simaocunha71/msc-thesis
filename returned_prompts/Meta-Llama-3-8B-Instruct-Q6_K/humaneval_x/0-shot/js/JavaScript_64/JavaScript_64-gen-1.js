```javascript
const vowelsCount = (s) => {
  let count = 0;
  for (let char of s.toLowerCase()) {
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
      count++;
    } else if (char === 'y' && s[s.length - 1] === 'y') {
      count++;
    }
  }
  return count;
};
```
Explanation:
The function `vowelsCount` takes a string `s` as input and returns the number of vowels in the string. To solve this problem, we use a for-of loop to iterate over each character in the string. We convert the string to lowercase to make the comparison case-insensitive. We then check if the character is a vowel ('a', 'e', 'i', 'o', 'u') or 'y' at the end of the string. If it is, we increment the count. Finally, we return the count. The condition `s[s.length - 1] === 'y'` checks if the character is 'y' and it is at the end of the string. This ensures that 'y' is only counted as a vowel if it is at the end of the string, as per the problem statement.