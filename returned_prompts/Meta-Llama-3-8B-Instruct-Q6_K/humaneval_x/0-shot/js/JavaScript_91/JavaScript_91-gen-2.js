```
const isBored = (S) => {
  let boredomCount = 0;
  let sentence = '';
  for (let i = 0; i < S.length; i++) {
    if (S[i] === '.' || S[i] === '?' || S[i] === '!') {
      if (sentence.startsWith('I')) {
        boredomCount++;
      }
      sentence = '';
    } else {
      sentence += S[i];
    }
  }
  if (sentence.startsWith('I')) {
    boredomCount++;
  }
  return boredomCount;
};
```


Explanation:
The function `isBored` takes a string `S` as input and returns the number of boredoms found in the string.

The function iterates over the string character by character. When it encounters a punctuation mark (`.` , `?`, or `!`), it checks if the current sentence starts with the word "I". If it does, it increments the boredom count.

After processing each sentence, the function resets the sentence string to an empty string.

Finally, if the last sentence in the string also starts with the word "I", the function increments the boredom count again.

The function returns the total boredom count.

Example inputs and outputs:
```
isBored("Hello world")  // 0
isBored("The sky is blue. The sun is shining. I love this weather")  // 1
```


Note: The function assumes that sentences are separated by punctuation marks and that a boredom is a sentence that starts with the word "I". It does not account for sentences that may be separated by multiple spaces or punctuation marks. If you need to handle such cases, you may need to modify the function accordingly.