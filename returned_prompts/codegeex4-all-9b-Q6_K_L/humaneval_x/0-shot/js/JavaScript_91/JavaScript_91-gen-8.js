You can use the `split` method to divide the string into sentences, then use the `filter` method to find sentences that start with "I". Finally, return the length of the filtered array.

Here's the updated code:

```javascript
const isBored = (S) => {
  const sentences = S.split(/[.!?]/).filter(sentence => sentence.trim().startsWith("I"));
  return sentences.length;
};
```

In this code, we use the regular expression `/[.!?]/` to split the string into sentences based on '.', '?' or '!'. The `trim` method is used to remove any leading or trailing whitespace from each sentence.