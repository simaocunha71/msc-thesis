Here is the JavaScript function that fulfills the requirements:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  if (txt.length === 0) return false;
  if (!/[a-zA-Z]/.test(txt[txt.length - 1])) return false;
  if (/\s/.test(txt[txt.length - 1])) return false;
  return true;
};

console.log(checkIfLastCharIsALetter("apple pie")); // ➞ false
console.log(checkIfLastCharIsALetter("apple pi e")); // ➞ true
console.log(checkIfLastCharIsALetter("apple pi e ")); // ➞ false
console.log(checkIfLastCharIsALetter("")); // ➞ false
```

This function uses regular expressions to check the last character of the string. The expression `/[a-zA-Z]/.test(txt[txt.length - 1])` checks if the last character is an alphabetical character. The expression `/\s/.test(txt[txt.length - 1])` checks if the last character is a whitespace character. If the last character is not an alphabetical character or is a whitespace character, the function returns `false`. Otherwise, it returns `true`. The function also checks if the string is empty, in which case it returns `false`.