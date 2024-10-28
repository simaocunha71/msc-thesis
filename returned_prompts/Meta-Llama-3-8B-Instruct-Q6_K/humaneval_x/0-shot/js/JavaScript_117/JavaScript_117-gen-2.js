Here is a JavaScript function that implements the described functionality:

```javascript
const selectWords = (s, n) => {
  const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';
  const words = s.split(' ');
  const result = [];

  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    let count = 0;

    for (let j = 0; j < word.length; j++) {
      if (consonants.includes(word[j])) {
        count++;
      }
    }

    if (count === n) {
      result.push(word);
    }
  }

  return result;
};
```

In this function, we first split the input string `s` into an array of words using the `split` method. We then iterate over each word in the array and count the number of consonants in the word using a nested loop. If the count of consonants is equal to `n`, we add the word to the result array. Finally, we return the result array.