You can use the `String.prototype.match()` method to check if the last character of the input string is an alphabetical character. This method returns an array containing matches of a pattern in a string. If no matches are found, it returns `null`.

You can also use the `String.prototype.trim()` method to remove any leading or trailing whitespace from the input string. This method returns a new string without the leading and trailing whitespace.

Here's the implementation for the `checkIfLastCharIsALetter()` function:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  const trimmedTxt = txt.trim();
  const lastChar = trimmedTxt[trimmedTxt.length - 1];
  const isLetter = /^[a-zA-Z]$/.test(lastChar);
  const isNotPartOfWord = trimmedTxt.match(/\b\w+\b/g) === null;
  return isLetter && isNotPartOfWord;
};
```

This function first trims the input string to remove any leading or trailing whitespace. Then it checks if the last character of the trimmed string is an alphabetical character using a regular expression. It also checks if the trimmed string contains any words by using the `\b\w+\b` pattern, which matches one or more word characters surrounded by word boundaries. If the trimmed string does not contain any words, the `match()` method returns `null`.

Finally, the function returns `true` if the last character is an alphabetical character and is not part of a word, and `false` otherwise.