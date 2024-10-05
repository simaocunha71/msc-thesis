Here is the solution to the problem. The idea is to use Kadane's algorithm, which is a dynamic programming algorithm used to find the maximum sum of a subarray within a one-dimensional array of numbers.

```
const minSubArraySum = (nums) => {
  let minSum = Infinity;
  let currentSum = 0;

  for (let num of nums) {
    currentSum = Math.min(num, currentSum + num);
    minSum = Math.min(minSum, currentSum);
  }

  return minSum;
};
```

This algorithm works by iterating over the array and at each step, it calculates the minimum sum of the current subarray. If the current number is less than the sum of the current subarray and the current number, it updates the sum. If the current sum is less than the minimum sum found so far, it updates the minimum sum.

For example, if we call `minSubArraySum([2, 3, 4, 1, 2, 4])`, the algorithm will iterate over the array as follows:

1. `currentSum` = 2, `minSum` = Infinity
2. `currentSum` = Math.min(3, 2 + 3) = 3, `minSum` = Infinity
3. `currentSum` = Math.min(4, 3 + 4) = 4, `minSum` = Infinity
4. `currentSum` = Math.min(1, 4 + 1) = 5, `minSum` = Infinity
5. `currentSum` = Math.min(2, 5 + 2) = 7, `minSum` = Infinity
6. `currentSum` = Math.min(4, 7 + 4) = 11, `minSum` = 7

The minimum sum found is 7, which is the minimum sum of any non-empty subarray of the input array.

The time complexity of this algorithm is O(n), where n is the length of the input array, because it needs to iterate over the array once. The space complexity is O(1), because it only uses a constant amount of space to store the minimum sum and the current sum.