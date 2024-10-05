```javascript
const findClosestElements = (numbers) => {
  numbers = numbers.slice().sort((a, b) => a - b);
  let minDiff = Infinity;
  let closestElements = [];
  for (let i = 0; i < numbers.length - 1; i++) {
    const diff = numbers[i + 1] - numbers[i];
    if (diff < minDiff) {
      minDiff = diff;
      closestElements = [numbers[i], numbers[i + 1]];
    }
  }
  return closestElements;
};
```


Explanation:

1.  We sort the list of numbers in ascending order to ensure that the closest elements are adjacent to each other.
2.  We initialize `minDiff` to Infinity and `closestElements` to an empty array.
3.  We iterate through the sorted list of numbers, calculating the difference between each pair of adjacent numbers.
4.  If the calculated difference is smaller than the current minimum difference, we update `minDiff` and set `closestElements` to the current pair of numbers.
5.  Finally, we return the `closestElements` array, which contains the two numbers that are closest to each other.

The function works correctly even when the input list contains duplicate numbers, as shown in the second test case. In this case, the function returns the duplicate number as the closest elements.