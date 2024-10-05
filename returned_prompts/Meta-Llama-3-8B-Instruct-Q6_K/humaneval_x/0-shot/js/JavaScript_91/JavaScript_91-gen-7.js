```
const isBored = (S) => {
  let boredomCount = 0;
  let sentence = '';

  for (let i = 0; i < S.length; i++) {
    if (S[i] === '.' || S[i] === '?' || S[i] === '!') {
      if (sentence.trim().startsWith('I')) {
        boredomCount++;
      }
      sentence = '';
    } else {
      sentence += S[i];
    }
  }

  if (sentence.trim().startsWith('I')) {
    boredomCount++;
  }

  return boredomCount;
};
```


Explanation:
We iterate over the input string `S` character by character. When we encounter a sentence delimiter ( '.', '?', or '!' ), we check if the current sentence starts with "I". If it does, we increment the boredom count. We then reset the sentence variable to an empty string. If the character is not a sentence delimiter, we add it to the sentence variable. After iterating over the entire string, we check one more time if the last sentence starts with "I" and increment the boredom count if it does. Finally, we return the boredom count.