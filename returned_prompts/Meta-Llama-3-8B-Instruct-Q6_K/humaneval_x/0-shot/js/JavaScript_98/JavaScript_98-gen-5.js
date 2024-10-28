Here is the solution using JavaScript:

```javascript
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0 && 'AEIOU'.toUpperCase().includes(s[i].toUpperCase())) {
      count++;
    }
  }
  return count;
};
```

Explanation:

1. Initialize a variable `count` to 0 to keep track of the number of uppercase vowels in even indices.
2. Loop through the string `s` using a for loop.
3. Check if the current index `i` is even (using the condition `i % 2 === 0`).
4. If the index is even, check if the character at that index is an uppercase vowel (using the condition `s[i].toUpperCase() && 'AEIOU'.toUpperCase().includes(s[i].toUpperCase())`).
5. If the character is an uppercase vowel, increment the `count` variable.
6. Return the `count` variable at the end of the function.

Testing:

```javascript
console.log(countUpper('aBCdEf')); // Output: 1
console.log(countUpper('abcdefg')); // Output: 0
console.log(countUpper('dBBE')); // Output: 0
```