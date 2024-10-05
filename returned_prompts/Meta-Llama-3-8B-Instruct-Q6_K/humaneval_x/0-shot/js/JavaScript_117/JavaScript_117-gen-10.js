Here is the solution using JavaScript:
```javascript
const selectWords = (s, n) => {
  const words = s.split(' ');
  const result = [];

  for (let i = 0; i < words.length; i++) {
    let consonants = 0;
    for (let j = 0; j < words[i].length; j++) {
      const char = words[i][j].toLowerCase();
      if (!['a', 'e', 'i', 'o', 'u'].includes(char) && !isNaN(Number(char))) {
        consonants++;
      }
    }
    if (consonants === n) {
      result.push(words[i]);
    }
  }
  return result;
};
```
Explanation:
The function `selectWords` takes a string `s` and a natural number `n` as input. It splits the string into words using the `split` method with a space character as the separator.

Then, it iterates over each word in the array of words using a `for` loop. For each word, it counts the number of consonants using another `for` loop. It checks each character in the word to see if it is a consonant (i.e., not a vowel and not a digit). If the character is a consonant, it increments the `consonants` counter.

Finally, if the `consonants` counter is equal to `n`, the word is added to the `result` array.

The function returns the `result` array, which contains all the words from the input string that contain exactly `n` consonants. If the input string is empty, the function returns an empty array.

You can test the function with the examples provided in the problem statement. For example, `selectWords("Mary had a little lamb", 4)` should return `["little"]`, and `selectWords("Hello world", 4)` should return `["world"]`.