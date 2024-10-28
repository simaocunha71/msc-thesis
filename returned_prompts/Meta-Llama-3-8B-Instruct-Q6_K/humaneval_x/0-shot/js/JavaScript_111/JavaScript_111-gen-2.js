```
const histogram = (test) => {
  if (!test) return {};
  let result = {};
  let maxCount = 0;
  let mostRepeatedLetters = [];

  test.split(' ').forEach((letter) => {
    if (!result[letter]) {
      result[letter] = 0;
    }
    result[letter]++;
    if (result[letter] > maxCount) {
      maxCount = result[letter];
      mostRepeatedLetters = [letter];
    } else if (result[letter] === maxCount) {
      mostRepeatedLetters.push(letter);
    }
  });

  return Object.fromEntries(mostRepeatedLetters.map((letter) => [letter, maxCount]));
};
```


This function first splits the input string into individual letters using the `split` method. It then iterates over the letters, keeping track of the count of each letter in the `result` object. If a letter has a count greater than the current maximum count, it updates the maximum count and resets the `mostRepeatedLetters` array to contain only that letter. If the count is equal to the maximum count, it adds the letter to the `mostRepeatedLetters` array.

Finally, it returns an object where the keys are the most repeated letters and the values are the maximum count. This is achieved by mapping the `mostRepeatedLetters` array to an array of key-value pairs and then converting this array to an object using the `Object.fromEntries` method. If no letters are present in the input string, the function returns an empty object.