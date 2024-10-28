The problem is to find the minimum sum of any non-empty sub-array of a given array of integers. This is a common problem in computer science and can be solved using various algorithms. One of the most efficient algorithms for this problem is the Kadane's algorithm, which runs in linear time.

Here's the implementation of Kadane's algorithm in JavaScript:

```javascript
const minSubArraySum = (nums) => {
  let minSum = Infinity;
  let currentSum = 0;

  for (let i = 0; i < nums.length; i++) {
    currentSum = Math.min(nums[i], currentSum + nums[i]);
    minSum = Math.min(minSum, currentSum);
  }

  return minSum;
};
```

Explanation:
1. Initialize `minSum` and `currentSum` to `Infinity` and `0` respectively.
2. Iterate through the array `nums` using a for loop.
3. For each element in the array, update `currentSum` to be the minimum of the current element and the sum of the current element and `currentSum`.
4. Update `minSum` to be the minimum of `minSum` and `currentSum`.
5. Return `minSum` as the result.

This algorithm works by keeping track of the minimum sum of the sub-array ending at each index. It updates the `currentSum` by comparing the current element with the sum of the current element and the previous `currentSum`. The `minSum` is updated to be the minimum of the current `minSum` and `currentSum` to keep track of the minimum sum of any sub-array encountered so far.

The time complexity of this algorithm is O(n), where n is the length of the input array `nums`.