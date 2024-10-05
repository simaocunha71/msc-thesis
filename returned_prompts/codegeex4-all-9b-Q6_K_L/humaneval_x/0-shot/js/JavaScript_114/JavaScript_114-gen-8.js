The problem requires finding the minimum sum of any non-empty sub-array of a given array of integers. 

To solve this problem, we can use Kadane's algorithm, which is a dynamic programming algorithm that can find the maximum sum sub-array in linear time. By modifying Kadane's algorithm to track the minimum sum instead of the maximum, we can solve this problem.

Here's the implementation of the function:

```javascript
const minSubArraySum = (nums) => {
  let minSum = nums[0];
  let currentSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentSum = Math.min(nums[i], currentSum + nums[i]);
    minSum = Math.min(minSum, currentSum);
  }

  return minSum;
};
```

The time complexity of this function is O(n), where n is the length of the input array. This is because we iterate through the array once, performing a constant amount of work for each element.

Let's test the function with the provided examples:

```javascript
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // Output: 1
console.log(minSubArraySum([-1, -2, -3])); // Output: -6
```

Both examples return the expected outputs.