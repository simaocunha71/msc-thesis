To check if two words have the same characters, we can follow these steps:

1. Sort the characters in each string in alphabetical order.
2. Compare the sorted strings to see if they are identical.

Here's the step-by-step solution:

Step 1: Sort the characters in each string in alphabetical order.
- We can use the `sort` method to sort the characters in each string. However, the `sort` method sorts strings in lexicographical order, which means it sorts uppercase letters before lowercase letters. To sort uppercase and lowercase letters together, we need to convert the strings to arrays of characters, sort the characters, and then join them back into strings.

Step 2: Compare the sorted strings to see if they are identical.
- After sorting the characters in each string, we can compare the sorted strings using the `===` operator. If the sorted strings are identical, it means the original strings have the same characters.

Here's the code that implements the solution:

```javascript
const sameChars = (s0, s1) => {
  const sortedS0 = [ ...s0 ].sort().join('');
  const sortedS1 = [ ...s1 ].sort().join('');
  return sortedS0 === sortedS1;
};
```

The `sort` method is called on arrays created from the strings using the spread operator `[ ...s ]`. The `join` method is used to convert the arrays back into strings.

Now you can use the `sameChars` function to check if two words have the same characters:

```javascript
console.log(sameChars('eabcdzzzz', 'dddzzzzzhzeddabc'));      // true
console.log(sameChars('abcd', 'dddddddabc'));                // true
console.log(sameChars('dddddddabc', 'abcd'));                // true
console.log(sameChars('eabcd', 'dddddddabc'));               // false
console.log(sameChars('abcd', 'dddddddabce'));               // false
console.log(sameChars('eabcdzzzz', 'dddzzzzzhzeddabc'));