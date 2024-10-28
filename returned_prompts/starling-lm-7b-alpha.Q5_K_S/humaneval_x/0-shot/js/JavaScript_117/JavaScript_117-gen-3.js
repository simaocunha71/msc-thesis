To solve this problem, we can follow these steps:

1. Define a function `isConsonant` that takes a character as input and returns `true` if the character is a consonant, and `false` otherwise. For example, we can consider all letters except 'a', 'e', 'i', 'o', 'u', and 'y' as consonants.

2. Initialize an empty list `result` to store the words that contain exactly `n` consonants.

3. Split the input string `s` into an array of words using the `split` method with space as the delimiter.

4. Iterate over each word in the array. For each word, check if the number of consonants in the word is equal to `n` by calling the `countConsonants` function. If the condition is true, add the word to the `result` list.

5. Return the `result` list.

Here's an example implementation of the `selectWords` function:

```javascript
function selectWords(s, n) {
  function isConsonant(char) {
    return !['a', 'e', 'i', 'o', 'u', 'y'].includes(char);
  }

  function countConsonants(word) {
    return word.split('').filter(isConsonant).length;
  }

  const result = [];
  const words = s.split(' ');

  words.forEach(word => {
    if (countConsonants(word) === n) {
      result.push(word);
    }
  });

  return result;
}
```

You can use this function to solve the problem by providing the input string `s` and the number of consonants `n` as arguments. The function will return a list of all the words from the input string that contain exactly `n` consonants, in the order they appear in the string.

*/

function selectWords(s, n) {
  function isConsonant(char) {
    return !['a', 'e', 'i', 'o', 'u', 'y'].includes(char);
  }

  function countConsonants(