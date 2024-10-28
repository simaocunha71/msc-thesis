You can split the string by the sentence delimiters, and then check if each sentence starts with the word "I". Here's how you can do it:

```javascript
const isBored = (S) => {
  const sentences = S.split(/[.?!]/).filter(Boolean);
  return sentences.filter(sentence => sentence.trim().startsWith('I')).length;
};
```

The `filter(Boolean)` function is used to remove any empty strings that may be left after splitting the string. The `trim()` function is used to remove any leading or trailing whitespace from each sentence before checking if it starts with "I".