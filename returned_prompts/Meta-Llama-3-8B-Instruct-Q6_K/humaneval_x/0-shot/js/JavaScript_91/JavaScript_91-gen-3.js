```
const isBored = (S) => {
  let boredoms = 0;
  let sentence = '';
  for (let i = 0; i < S.length; i++) {
    if (S[i] === '.' || S[i] === '?' || S[i] === '!') {
      if (sentence.startsWith('I')) {
        boredoms++;
      }
      sentence = '';
    } else {
      sentence += S[i];
    }
  }
  if (sentence.startsWith('I')) {
    boredoms++;
  }
  return boredoms;
};
``` 