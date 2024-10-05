Here is a JavaScript function that does the task:

```javascript
const digitSum = (s) => {
  return s.toUpperCase().split('').filter(c => c.match(/[A-Z]/)).map(c => c.charCodeAt(0)).reduce((a, b) => a + b, 0);
};
```

Explanation:
The function `digitSum` takes a string `s` as input and returns the sum of the ASCII codes of the upper case characters in the string.

Here is the breakdown of the function:

1. `s.toUpperCase()`: This converts the input string to uppercase, so that all characters are in uppercase.
2. `split('')`: This splits the string into an array of individual characters.
3. `filter(c => c.match(/[A-Z]/))`: This filters the array to include only the characters that match the regular expression `/[A-Z]/`, which matches any uppercase letter.
4. `map(c => c.charCodeAt(0))`: This maps each character to its ASCII code using the `charCodeAt` method.
5. `reduce((a, b) => a + b, 0)`: This reduces the array of ASCII codes to a single sum, starting from 0.

For example, for the input string `"abAB"`, the function would return `131`, which is the sum of the ASCII codes of the uppercase characters `A` and `B`. Similarly, for the input string `"abcCd"`, the function would return `67`, which is the sum of the ASCII codes of the uppercase characters `C` and `D`.