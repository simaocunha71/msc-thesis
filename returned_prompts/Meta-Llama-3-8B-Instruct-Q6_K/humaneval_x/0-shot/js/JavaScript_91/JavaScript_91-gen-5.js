```
function isBored(S) {
  return S.split('.').filter(sentence => sentence.trim().startsWith('I')).length;
}
```



Explanation:
- We split the input string `S` into an array of sentences using the dot (.) as a delimiter.
- We then filter this array to only include sentences that start with the word "I" (ignoring case) using the `trim()` method to remove any leading or trailing whitespace.
- Finally, we return the length of the filtered array, which represents the number of boredoms.