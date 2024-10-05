```javascript
function findClosestElements(numbers) {
  const sortedNumbers = numbers.slice().sort((a, b) => a - b);
  let closestPair = [sortedNumbers[0], sortedNumbers[1]];
  let minDiff = Math.abs(sortedNumbers[1] - sortedNumbers[0]);

  for (let i = 1; i < sortedNumbers.length - 1; i++) {
    const diff = Math.abs(sortedNumbers[i + 1] - sortedNumbers[i]);
    if (diff < minDiff) {
      minDiff = diff;
      closestPair = [sortedNumbers[i], sortedNumbers[i + 1]];
    }
  }

  return closestPair;
}

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])); // (2.0, 2.2)
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])); // (2.0, 2.0)
```
In this solution, we first sort the input list of numbers in ascending order. Then we initialize a variable `closestPair` with the first two elements of the sorted list and a variable `minDiff` with the difference between the first two elements. We then iterate through the list starting from the second element (index 1) to the second last element (index `length - 2`). For each element, we calculate the difference with the next element and if this difference is less than the current `minDiff`, we update `minDiff` and `closestPair`. Finally, we return `closestPair`. This solution has a time complexity of O(n log n) due to the sorting operation. If the list is already sorted, the time complexity can be reduced to O(n). 

Note that the problem does not specify whether to consider duplicates or not. In this solution, duplicates are considered, so if there are multiple pairs with the same minimum difference, the first one encountered is returned. If you want to return all pairs with the minimum difference, you would need to modify the solution accordingly. 

Also, this solution assumes that the input list has at least two elements. If the input list can have less than two elements, you would need to add error handling to handle this case. 