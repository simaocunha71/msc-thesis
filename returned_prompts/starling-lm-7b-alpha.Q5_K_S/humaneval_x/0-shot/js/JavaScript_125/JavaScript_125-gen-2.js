To solve this problem we can follow these steps:

1. Check if there are any whitespaces in the string. If so, split the string on whitespaces and return the result.
2. If there are no whitespaces in the string, check if there are any commas in the string. If so, split the string on commas and return the result.
3. If there are neither whitespaces nor commas in the string, count the number of lower-case letters with odd order in the alphabet and return the result.

Here's a step-by-step breakdown of the solution:

1. First, we check if the string contains any whitespaces using the `includes` method. If it does, we split the string on whitespaces using the `split` method with a whitespace argument and return the result.
2. If there are no whitespaces in the string, we check if the string contains any commas using the `includes` method. If it does, we split the string on commas using the `split` method with a comma argument and return the result.
3. If there are neither whitespaces nor commas in the string, we initialize a variable `count` to 0. Then, we iterate over each character in the string using the `forEach` method. For each character, we check if it is a lower-case letter using the `charCodeAt` method and the `charCodeAt` method. If it is, we check if its ASCII code is odd using the modulo operator `%`. If it is, we increment the `count` variable by 1. Finally, we return the `count` variable.

Here's the code for the solution:

```javascript
const splitWords = (txt) => {
  const words = txt.includes(' ') ? txt.split(' ') : (txt.includes(',') ? txt.split(',') : txt.match(/[a-z]/g).filter(c => c.charCodeAt(0) % 2 === 1).length);
  return words;
}
```

This solution should pass all the provided examples and handle any edge cases that may arise.

*/

```javascript
const splitWords = (txt) => {
  const words = txt.includes(' ') ? txt.split(' ')