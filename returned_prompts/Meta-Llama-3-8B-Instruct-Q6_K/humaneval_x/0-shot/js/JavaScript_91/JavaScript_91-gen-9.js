```
const isBored = (S) => {
  return S.split('.').filter(sentence => sentence.trim().startsWith('I')).length;
};
```

Explanation:
The function `isBored` takes a string `S` as input. It splits the string into sentences using the `split` method with a regex pattern that matches the characters `.`, `?`, and `!` as sentence delimiters.

It then uses the `filter` method to iterate over the sentences and checks if each sentence starts with the word "I" using the `startsWith` method. The `trim` method is used to remove any leading or trailing whitespace from the sentence.

The `filter` method returns a new array containing all the sentences that start with "I". The `length` property of this array is then returned, which represents the number of boredoms in the input string.