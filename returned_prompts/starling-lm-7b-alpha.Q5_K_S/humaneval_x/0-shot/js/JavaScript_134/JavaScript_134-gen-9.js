To solve this problem, you can follow these steps:

1. Check if the last character of the string is an alphabetical character. You can use the `charCodeAt()` method to get the ASCII code of the last character, and then check if it falls within the range of lowercase or uppercase alphabets. For lowercase, the range is 97 to 122, and for uppercase, the range is 65 to 90.

2. If the last character is an alphabetical character, move to step 3. Otherwise, return false.

3. Check if the last character is a part of a word. You can do this by iterating through the string from the second-to-last character to the first character, and checking if each character is an alphabetical character. If you find a non-alphabetical character, return false. Otherwise, return true.

Here's the code that implements these steps:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  const lastChar = txt.charCodeAt(txt.length - 1);

  if (lastChar < 97 || lastChar > 122 && lastChar < 65 || lastChar > 90) {
    return false;
  }

  let isLastCharInWord = false;
  for (let i = txt.length - 2; i >= 0; i--) {
    const char = txt.charCodeAt(i);
    if (!(char < 97 || char > 122 && char < 65 || char > 90)) {
      isLastCharInWord = true;
      break;
    }
  }

  return isLastCharInWord;
};
```

You can use this function to check if the last character of a string is an alphabetical character and is not a part of a word. For example:

```javascript
console.log(checkIfLastCharIsALetter("apple pie"));       // Output: false
console.log(checkIfLastCharIsALetter("apple pi e"));      // Output: true
console.log(checkIfLastCharIsALetter("apple pi e "));    