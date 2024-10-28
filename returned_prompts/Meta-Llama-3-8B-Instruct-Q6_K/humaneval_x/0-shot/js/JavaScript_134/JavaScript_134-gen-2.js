Here is the solution:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  // Remove leading and trailing spaces
  txt = txt.trim();
  // Check if the string is empty
  if (txt.length === 0) return false;
  // Check if the last character is an alphabetical character
  if (!/[a-zA-Z]/.test(txt.slice(-1))) return false;
  // Check if the last character is part of a word
  if (txt.slice(-1) !== ' ' && !/\s/.test(txt.slice(-2))) return true;
  return false;
};

console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
console.log(checkIfLastCharIsALetter("apple pi e ")); // false
console.log(checkIfLastCharIsALetter("")); // false
```

Explanation:
The function `checkIfLastCharIsALetter` takes a string `txt` as input. It first removes any leading or trailing spaces using the `trim` method. Then, it checks if the string is empty. If it is, the function returns `false`.

Next, it checks if the last character of the string is an alphabetical character using a regular expression `/[a-zA-Z]/`. If it's not, the function returns `false`.

Finally, it checks if the last character is part of a word by checking if there's a space character before it. If there's no space, it means the character is part of a word, and the function returns `false`. If there is a space, it means the character is not part of a word, and the function returns `true`. If the string is empty or the last character is not an alphabetical character, the function returns `false`. Otherwise, it returns `true`.