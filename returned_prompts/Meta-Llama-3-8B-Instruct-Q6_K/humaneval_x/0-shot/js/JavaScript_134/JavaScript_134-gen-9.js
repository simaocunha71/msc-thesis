Here is a JavaScript function that solves the problem:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  if (txt === "") return false;
  let lastChar = txt.charAt(txt.length - 1);
  if (!/[a-zA-Z]/.test(lastChar)) return false;
  if (txt.charAt(txt.length - 2) === " " || txt.charAt(txt.length - 2) === "") return false;
  return true;
};
```
This function checks the last character of the given string. If the last character is not an alphabetical character, it returns `false`. If the last character is an alphabetical character, it checks if the character before it is a space or an empty string. If it is, it returns `false`. Otherwise, it returns `true`. The function also handles the case where the input string is empty by returning `false`.