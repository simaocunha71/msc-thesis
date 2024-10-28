```javascript
const histogram = (test) => {
  let frequency = {};
  if (test === '') {
    return frequency;
  }
  let words = test.split(' ');
  for (let word of words) {
    if (word in frequency) {
      frequency[word]++;
    } else {
      frequency[word] = 1;
    }
  }
  let maxCount = Math.max(...Object.values(frequency));
  let result = {};
  for (let key in frequency) {
    if (frequency[key] === maxCount) {
      result[key] = maxCount;
    }
  }
  return result;
};
```
Explanation:
1. Initialize an empty object `frequency` to store the frequency of each letter.
2. Split the input string `test` into an array of words using the `split` method.
3. Iterate through each word in the array and update the frequency of each letter in the `frequency` object.
4. Find the maximum frequency using the `Math.max` function and the `Object.values` method.
5. Iterate through the `frequency` object and add the letters with the maximum frequency to the `result` object.
6. Return the `result` object. If the input string is empty, return an empty object.