```
  let minDistance = Infinity;
  let closestElements = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      const distance = Math.abs(numbers[i] - numbers[j]);
      if (distance < minDistance) {
        minDistance = distance;
        closestElements = [numbers[i], numbers[j]].sort((a, b) => a - b);
      }
    }
  }

  return closestElements;
```
Explanation:
This function iterates over the list of numbers and calculates the absolute difference between each pair of numbers. It keeps track of the smallest difference found so far and the corresponding pair of numbers. After iterating over all pairs, it returns the pair of numbers that are closest to each other. The pair is sorted in ascending order. If there are multiple pairs with the same smallest distance, the function will return one of them.

For example, in the test case `findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])`, the function will iterate over the pairs `(1.0, 2.0)`, `(1.0, 2.2)`, `(1.0, 3.0)`, ... and find that the pair `(2.0, 2.2)` has the smallest distance. The function will return this pair in ascending order, which is `(2.0, 2.2)`. Similarly, in the test case `findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])`, the function will find that the pair `(2.0, 2.0)` has the smallest distance and return it in ascending order, which is also `(2.0, 2.0)`.