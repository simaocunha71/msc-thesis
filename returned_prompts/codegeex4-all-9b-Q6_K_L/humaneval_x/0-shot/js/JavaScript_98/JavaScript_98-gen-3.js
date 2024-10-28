You can solve this problem by iterating over the characters of the string, checking if they are uppercase vowels and if their index is even. Here is a possible implementation in JavaScript:

```javascript
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0) {
      if (s[i] === 'A' || s[i] === 'E' || s[i] === 'I' || s[i] === 'O' || s[i] === 'U') {
        count++;
      }
    }
  }
  return count;
};
```

This solution iterates over the characters of the string, checking if their index is even and if they are an uppercase vowel. If both conditions are met, the count is incremented. Finally, the function returns the count.

Here are some examples of how the function works:

```javascript
console.log(countUpper('aBCdEf')); // 1
console.log(countUpper('abcdefg')); // 0
console.log(countUpper('dBBE')); // 0
```

In the first example, the uppercase vowel 'E' is at index 2, which is even. Therefore, the count is incremented and the function returns 1.

In the second example, there are no uppercase vowels at even indices. Therefore, the count remains 0 and the function returns 0.

In the third example, there are no uppercase vowels at even indices. Therefore, the count remains 0 and the function returns 0.