To solve this problem, we can use a dynamic programming approach. We will iterate through the array and maintain a running sum of the subarray. If the running sum becomes negative, we reset it to 0. We will also keep track of the minimum sum encountered so far.

Here is the implementation in JavaScript:

```javascript
const minSubArraySum = (nums) => {
  let minSum = Infinity;
  let currentSum = 0;

  for (let i = 0; i < nums.length; i++) {
    currentSum += nums[i];
    if (currentSum < minSum) {
      minSum = currentSum;
    }
    if (currentSum > 0) {
      currentSum = 0;
    }
  }

  return minSum;
};
```

Let's test the function with the given examples:

```javascript
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // Output: 1
console.log(minSubArraySum([-1, -2, -3])); // Output: -6
```

The function returns the expected results for both examples.