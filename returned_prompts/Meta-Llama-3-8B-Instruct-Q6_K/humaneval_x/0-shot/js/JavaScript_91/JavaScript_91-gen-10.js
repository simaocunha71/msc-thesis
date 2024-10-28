```
function isBored(S) {
  const sentences = S.split(/[.!?]/);
  let boredCount = 0;
  for (const sentence of sentences) {
    if (sentence.trim().startsWith('I')) {
      boredCount++;
    }
  }
  return boredCount;
}
```


Explanation:
The function `isBored` takes a string `S` as input. It splits the string into an array of sentences using a regular expression that matches '.', '?', and '!'. Then it iterates over the sentences, trimming each sentence to remove any leading or trailing whitespace. If a sentence starts with the word 'I', it increments the `boredCount`. Finally, it returns the `boredCount`. If no sentences start with 'I', it returns 0.