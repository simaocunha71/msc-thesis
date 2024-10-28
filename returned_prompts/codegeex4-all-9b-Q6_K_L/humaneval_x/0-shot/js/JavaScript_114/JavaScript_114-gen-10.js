The problem asks to find the minimum sum of any non-empty sub-array of an array of integers. 

Here is a JavaScript solution using Kadane's algorithm:

```javascript
const minSubArraySum = (nums) => {
  let minSum = nums[0];
  let currentSum = nums[0];
  
  for (let i = 1; i < nums.length; i++) {
    currentSum = Math.min(nums[i], currentSum + nums[i]);
    minSum = Math.min(minSum, currentSum);
  }
  
  return minSum;
}
```

Explanation:

The algorithm maintains two variables `minSum` and `currentSum`. `minSum` keeps track of the minimum sum found so far, and `currentSum` keeps track of the current sub-array sum.

The algorithm iterates over the array, and for each element, it updates `currentSum` to be the minimum of the current element and the sum of the current element and `currentSum`. This is done because if the current element is smaller than the sum of the current element and `currentSum`, then it is better to start a new sub-array with the current element.

Then, the algorithm updates `minSum` to be the minimum of `minSum` and `currentSum`. This is done because if the current `currentSum` is smaller than `minSum`, then the current sub-array sum is the minimum sum found so far.

Finally, the algorithm returns `minSum`, which is the minimum sum of any non-empty sub-array of `nums`.