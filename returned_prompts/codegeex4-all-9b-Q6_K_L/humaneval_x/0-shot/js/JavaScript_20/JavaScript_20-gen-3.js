```js
const findClosestElements = (numbers) => {
  let minDiff = Infinity;
  let result = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      const diff = Math.abs(numbers[i] - numbers[j]);
      if (diff < minDiff) {
        minDiff = diff;
        result = [numbers[i], numbers[j]];
      }
    }
  }

  return result.sort((a, b) => a - b);
}
```
This solution uses a nested loop to compare all pairs of numbers in the given list. It keeps track of the smallest difference found so far and updates the result whenever a smaller difference is found. Finally, it sorts the result in ascending order and returns it.