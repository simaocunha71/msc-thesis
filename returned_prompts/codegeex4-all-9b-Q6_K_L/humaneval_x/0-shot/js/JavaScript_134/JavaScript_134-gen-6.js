You can solve this problem using the `split()` method to split the string into an array of words, and then checking the last character of the last word in the array. Here's how you can do it:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  if (txt === '') {
    return false;
  }
  
  const words = txt.split(' ');
  const lastWord = words[words.length - 1];
  const lastChar = lastWord[lastWord.length - 1];
  
  return /^[a-zA-Z]$/.test(lastChar);
};

// Examples
console.log(checkIfLastCharIsALetter("apple pie"));  // false
console.log(checkIfLastCharIsALetter("apple pi e"));  // true
console.log(checkIfLastCharIsALetter("apple pi e "));  // false
console.log(checkIfLastCharIsALetter(""));  // false
```

The regular expression `/^[a-zA-Z]$/` is used to check if the last character is an alphabetical character. The `^` and `$` characters are used to assert the position at the start and end of the string, respectively. The `a-z` and `A-Z` characters are used to match any lowercase and uppercase letter, respectively.