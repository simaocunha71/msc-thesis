```
function findClosestElements(numbers) {
  let minDiff = Infinity;
  let closestElements = [];
  numbers.forEach((num, i) => {
    for (let j = i + 1; j < numbers.length; j++) {
      const diff = Math.abs(num - numbers[j]);
      if (diff < minDiff) {
        minDiff = diff;
        closestElements = [num, numbers[j]];
      }
    }
  });
  return closestElements;
}
```


Here's a breakdown of the solution:
1.  Initialize `minDiff` to infinity, which will be used to track the minimum difference between any two numbers.
2.  Initialize an empty array `closestElements` to store the two closest numbers.
3.  Iterate through the input array `numbers` using `forEach`.
4.  For each number, iterate through the remaining numbers in the array (starting from the next index `i + 1`) using a nested loop.
5.  Calculate the absolute difference `diff` between the current number and the other number.
6.  If `diff` is less than `minDiff`, update `minDiff` and set `closestElements` to the current number and the other number.
7.  After iterating through all numbers, return the `closestElements` array, which contains the two closest numbers in order (smaller number, larger number).

This solution has a time complexity of O(n^2), where n is the length of the input array, because it uses a nested loop to iterate through the array. However, this is the most straightforward way to solve the problem. If you need a more efficient solution, you can consider using a different approach, such as sorting the array and then finding the closest elements.