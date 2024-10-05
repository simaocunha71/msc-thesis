```js
const findClosestElements = (numbers) => {
  let smallestDifference = Infinity;
  let closestPair = null;

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      const difference = Math.abs(numbers[i] - numbers[j]);
      if (difference < smallestDifference) {
        smallestDifference = difference;
        closestPair = [numbers[i], numbers[j]].sort((a, b) => a - b);
      }
    }
  }

  return closestPair;
}
```
