Here is the JavaScript solution for the problem:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  if (txt === "") {
    return false;
  }
  const lastChar = txt.slice(-1);
  const words = txt.split(" ");
  if (words[words.length - 1].slice(-1) === lastChar) {
    return false;
  }
  return !isNaN(lastChar) && /^[a-zA-Z]+$/.test(lastChar);
};
```

Explanation:
1. The function takes a string as an argument.
2. It checks if the string is empty. If it is, the function returns false.
3. It extracts the last character of the string using the slice method.
4. It splits the string into words using the split method.
5. It checks if the last character of the last word is the same as the last character of the string. If it is, the function returns false.
6. It checks if the last character is a number or not using the isNaN method. If it is a number, the function returns false.
7. It checks if the last character is an alphabetical character using the test method with a regular expression. If it is not, the function returns false.
8. If all the above conditions are met, the function returns true, indicating that the last character is an alphabetical character and is not a part of a word.