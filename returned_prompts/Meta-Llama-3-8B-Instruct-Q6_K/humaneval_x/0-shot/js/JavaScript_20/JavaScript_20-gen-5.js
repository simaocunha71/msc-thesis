```javascript
function findClosestElements(numbers) {
  // sort the numbers
  numbers.sort((a, b) => a - b);

  // find the closest pair
  let closestPair = [numbers[0], numbers[1]];
  let closestDiff = Math.abs(closestPair[1] - closestPair[0]);

  for (let i = 1; i < numbers.length - 1; i++) {
    let diff = Math.abs(numbers[i + 1] - numbers[i]);
    if (diff < closestDiff) {
      closestPair = [numbers[i], numbers[i + 1]];
      closestDiff = diff;
    }
  }

  return closestPair;
}

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]));  // (2.0, 2.2)
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]));  // (2.0, 2.0)
```

The code first sorts the list of numbers. Then it initializes the closest pair to the first two numbers in the list. It then iterates over the list, checking each pair of adjacent numbers to see if they are closer to each other than the current closest pair. If they are, it updates the closest pair. Finally, it returns the closest pair. This has a time complexity of O(n log n) due to the sorting step, where n is the length of the list of numbers. The space complexity is O(1) since it only uses a constant amount of space. 

The problem statement does not specify what to do if there are multiple pairs of numbers that are equally close to each other. In this implementation, it returns the first pair it finds that is as close as the closest pair it has found so far. If you want to return all pairs that are as close as the closest pair, you would need to modify the code to keep track of all such pairs. 