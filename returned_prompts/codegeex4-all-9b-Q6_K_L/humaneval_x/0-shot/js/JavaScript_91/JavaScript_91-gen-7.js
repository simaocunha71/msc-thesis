You can solve this by splitting the string into sentences, and then checking if each sentence starts with "I".

Here's a possible solution:

```javascript
const isBored = (S) => {
  const sentences = S.split(/[.?!]/);
  return sentences.filter(sentence => sentence.trim().startsWith("I")).length;
}
```

In this solution, we use the `split()` method to split the string into an array of sentences, using the regular expression `[.?!]` as the delimiter. We then use the `filter()` method to create a new array of sentences that start with "I". Finally, we return the length of this new array, which is the number of boredoms.