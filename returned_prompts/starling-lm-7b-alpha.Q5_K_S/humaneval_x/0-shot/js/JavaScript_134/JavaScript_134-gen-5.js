To solve this problem we can follow these steps:

1. First, we can check if the last character of the string is an alphabetical character. We can do this using the `charCodeAt()` method, which returns the Unicode value of the character at the specified index. If the Unicode value of the last character is between 65 and 90 (inclusive), it is an uppercase letter, and if the Unicode value is between 97 and 122 (inclusive), it is a lowercase letter.

2. Next, we can check if the last character is a part of a word. We can do this by checking if the last character is followed by one or more alphanumeric characters (i.e., letters or numbers). We can use a regular expression to check this.

Here's how we can implement the function:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  const lastChar = txt[txt.length - 1];
  const isLetter = (lastChar >= 'A' && lastChar <= 'Z') || (lastChar >= 'a' && lastChar <= 'z');
  const isNotPartOfWord = /\s\w*$/.test(txt);

  return isLetter && isNotPartOfWord;
}
```

In this implementation, we first extract the last character of the string using `txt[txt.length - 1]`. We then use a ternary operator to check if the last character is a letter. If it is, we proceed to the next step. If it's not, we immediately return false.

Next, we use a regular expression `/\s\w*$/` to check if the last character is followed by one or more alphanumeric characters. The `\s` matches any whitespace character, and `\w*` matches zero or more alphanumeric characters. The `$` anchor ensures that we're only matching characters at the end of the string. The `test()` method of the regular expression object returns true if there is a match, and false otherwise.

Finally, we return the result of the logical AND operation between `isLetter` and `isNotPartOfWord`. If both conditions are true, the function returns true; otherwise,