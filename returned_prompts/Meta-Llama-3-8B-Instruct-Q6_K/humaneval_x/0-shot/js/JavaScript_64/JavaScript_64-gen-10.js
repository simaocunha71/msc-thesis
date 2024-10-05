Here is a JavaScript solution for the problem:
```javascript
const vowelsCount = (s) => {
  let count = 0;
  for (let char of s.toLowerCase()) {
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u' || char === 'y' && s.indexOf(char) === s.length - 1) {
      count++;
    }
  }
  return count;
};
```
Here's an explanation of the solution:

1. We initialize a variable `count` to 0 to keep track of the number of vowels.
2. We iterate through each character `char` in the input string `s` using a `for...of` loop.
3. We convert the character to lowercase using `toLowerCase()` to ensure the comparison is case-insensitive.
4. We check if the character is a vowel ('a', 'e', 'i', 'o',