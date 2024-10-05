To solve this problem, you need to split the string into sentences based on the delimiters '.', '?' and '!', then check if each sentence starts with the word "I". Here's the implementation:

```javascript
const isBored = (S) => {
  // Split the string into sentences based on the delimiters
  const sentences = S.split(/[.?!]/);

  // Filter the sentences that start with "I"
  const boredSentences = sentences.filter(sentence => sentence.trim().startsWith("I"));

  // Return the number of bored sentences
  return boredSentences.length;
}
```

This function takes the input string `S` and splits it into an array of sentences using the regular expression `[.?!]`. Then, it filters the array to keep only the sentences that start with "I" (after trimming any leading or trailing whitespace). Finally, it returns the number of bored sentences by getting the length of the filtered array.