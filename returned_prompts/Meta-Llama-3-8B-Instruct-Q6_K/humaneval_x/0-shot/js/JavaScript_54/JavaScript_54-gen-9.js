Here is the solution:
```javascript
const sameChars = (s0, s1) => {
  return s0.split('').sort().join('') === s1.split('').sort().join('');
};
```
Here's an explanation of the code:

1. `s0.split('')` and `s1.split('')` split the strings into individual characters, creating arrays of characters.
2. `sort()` sorts the arrays of characters in lexicographic order.
3. `join('')` concatenates the sorted arrays back into strings, without any separator.
4. The `===` operator checks if the two resulting strings are identical.

By sorting the characters and comparing the resulting strings, we can ignore the order of the characters in the original strings and focus on the presence or absence of each character. This allows us to determine if two words have the same characters, regardless of their order.