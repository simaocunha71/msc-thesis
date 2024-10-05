To solve this problem we can follow these steps:

1. First, we need to check if the last character of the string is an alphabetical character. We can use the `charCodeAt()` method to get the ASCII code of the last character and then check if it is within the range of lowercase or uppercase alphabetical characters.

2. Next, we need to check if the last character is not a part of a word. We can split the string using the space character as the delimiter and check if the last element of the resulting array is the same as the last character of the original string.

3. If both conditions are true, we return `true`, otherwise we return `false`.

Here's the implementation of the `checkIfLastCharIsALetter` function:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  const lastCharCode = txt.charCodeAt(txt.length - 1);
  const isLetter = (lastCharCode >= 65 && lastCharCode <= 90) || (lastCharCode >= 97 && lastCharCode <= 122);
  const isLastCharInWord = txt.split(' ')[txt.split(' ').length - 1] === txt[txt.length - 1];

  return isLetter && !isLastCharInWord;
};
```

This implementation first gets the ASCII code of the last character of the string using the `charCodeAt()` method. It then checks if the ASCII code is within the range of lowercase or uppercase alphabetical characters. Next, it splits the string using the space character as the delimiter and checks if the last element of the resulting array is the same as the last character of the original string. If both conditions are true, it returns `true`, otherwise it returns `false`.

You can use this function to check if the last character of a given string is an alphabetical character and is not a part of a word.

For example:

```javascript
console.log(checkIfLastCharIsALetter("apple pie"));  // Output: false
console.log(checkIfLastCharIsALetter("apple pi e"));  // Output: true
console.log