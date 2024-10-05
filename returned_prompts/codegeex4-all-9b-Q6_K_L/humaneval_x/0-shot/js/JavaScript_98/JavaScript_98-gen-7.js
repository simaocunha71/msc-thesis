You can solve this problem using the following approach:

1. Iterate through the string `s` with a loop.
2. For each character, check if it is an uppercase vowel (A, E, I, O, U).
3. If the character is an uppercase vowel and its index is even, increment a counter variable.
4. Return the counter variable as the result.

Here is the implementation of the `countUpper` function in JavaScript:

```javascript
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0 && 'AEIOU'.includes(s[i])) {
      count++;
    }
  }
  return count;
}
```

You can test the function with the provided examples:

```javascript
console.log(countUpper('aBCdEf')); // 1
console.log(countUpper('abcdefg')); // 0
console.log(countUpper('dBBE')); // 0
```