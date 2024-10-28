The solution is quite straightforward. We can iterate over the string using a for loop and check if the character at the current index is an uppercase vowel and if the index is even. If both conditions are met, we increment the count.

Here's the code:

```javascript
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0 && /[AEIOU]/.test(s[i].toUpperCase())) {
      count++;
    }
  }
  return count;
};
```

In this code, `i % 2 === 0` checks if the index is even, and `/[AEIOU]/.test(s[i].toUpperCase())` checks if the character at the current index is an uppercase vowel. The `toUpperCase()` function is used to ensure that we're checking for uppercase vowels, regardless of whether the character in the string is uppercase or lowercase.

The function returns the count of uppercase vowels in even indices. For example, `countUpper('aBCdEf')` returns 1, `countUpper('abcdefg')` returns 0, and `countUpper('dBBE')` returns 0.