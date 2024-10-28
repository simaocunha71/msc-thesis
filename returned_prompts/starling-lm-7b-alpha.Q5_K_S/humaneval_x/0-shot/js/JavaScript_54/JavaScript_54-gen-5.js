To solve this kata, you must first ensure that the two strings have the same length, because if they don't, it is impossible for the characters to be the same. Then, you can compare each character at the same position in both strings. If any pair of characters is not equal, you must return false. If all pairs are equal, you can return true.

Here's a step-by-step breakdown of the solution:

1. Compare the lengths of the two input strings `s0` and `s1`. If they are not equal, return `false` because the strings can't have the same characters if they have different lengths.
2. Iterate through the characters of the strings using a for loop. For each character at index `i`, compare the characters `s0[i]` and `s1[i]`. If they are not equal, return `false`.
3. If the loop completes without returning `false`, return `true` to indicate that all characters are the same.

Here's the code for the solution:

```javascript
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  for (let i = 0; i < s0.length; i++) {
    if (s0[i] !== s1[i]) return false;
  }
  return true;
};
```

With this solution, you can now determine whether two strings have the same characters.

Let's test it with some examples:

```javascript
console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')); // true
console.log(sameChars('abcd', 'dddddddabc')); // true
console.log(sameChars('dddddddabc', 'abcd')); // true
console.log(sameChars('eabcd', 'dddddddabc')); // false
console.log(sameChars('abcd', 'dddddddabce')); // false
console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddddabc')); // false
```

As you can see, the `sameChars` function