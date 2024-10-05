The countUpper function checks the characters at even indices of the string and counts how many of them are uppercase vowels. The function takes a string as an argument and returns an integer.

Here is the solution to the problem:

```javascript
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i += 2) {
    if (s[i] === 'A' || s[i] === 'E' || s[i] === 'I' || s[i] === 'O' || s[i] === 'U') {
      count++;
    }
  }
  return count;
};
```
Explanation:

1. We initialize a count variable to 0.
2. We loop through the string, checking each character at an even index (i.e., 0, 2, 4, ...).
3. If the character at the even index is an uppercase vowel (i.e., 'A', 'E', 'I', 'O', or 'U'), we increment the count variable.
4. Finally, we return the count variable, which represents the number of uppercase vowels in even indices of the string.