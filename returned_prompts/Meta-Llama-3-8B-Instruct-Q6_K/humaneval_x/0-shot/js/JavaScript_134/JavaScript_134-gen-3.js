Here is a JavaScript function that solves the problem:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  if (txt.length === 0) return false;
  const lastChar = txt.trim().slice(-1);
  return /^[a-zA-Z]$/.test(lastChar);
};
```

Explanation:
- We first check if the input string is empty, if so, we return false.
- Then we use the `trim()` method to remove any leading or trailing whitespace from the string.
- We use the `slice(-1)` method to get the last character of the string.
- Finally, we use a regular expression to check if the last character is an alphabetical character. The regular expression `/^[a-zA-Z]$/.test(lastChar)` checks if the last character is either uppercase or lowercase letter. If it is, we return true, otherwise, we return false.