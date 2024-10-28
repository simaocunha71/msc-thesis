```js
const findClosestElements = (numbers) => {
  // Sort the array in ascending order
  const sortedNumbers = numbers.slice().sort((a, b) => a - b);
  // Initialize the smallest difference to a large number
  let smallestDifference = Number.MAX_VALUE;
  // Initialize the closest pair of numbers
  let closestPair = [sortedNumbers[0], sortedNumbers[1]];

  // Iterate through the array to find the closest pair
  for (let i = 0; i < sortedNumbers.length - 1; i++) {
    const difference = sortedNumbers[i + 1] - sortedNumbers[i];
    if (difference < smallestDifference) {
      smallestDifference = difference;
      closestPair = [sortedNumbers[i], sortedNumbers[i + 1]];
    }
  }

  return closestPair;
};
```

This solution works by first sorting the array in ascending order. Then, it iterates through the array to find the pair of numbers with the smallest difference. The time complexity of this solution is O(n log n) due to the sorting step.