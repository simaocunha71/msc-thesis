  let minSum = Infinity;
  let currentSum = 0;

  for (let num of nums) {
    currentSum += num;
    minSum = Math.min(minSum, currentSum);
    currentSum = Math.min(currentSum, 0);
  }

  return minSum;
};

console.log(minSubArraySum([2, -3, 4, -1, 2, 4])); // -6
console.log(minSubArraySum([-2, -3, -4, -1, -2, -4])); // -10

// Explanation:
// The sub-array with the minimum sum is [2, -3, 4, -1, 2, 4] which sums to 1.
// The sub-array with the minimum sum is [-2, -3, -4, -1, -2, -4] which sums to -10.
```

#### 2.1.4. 使用 JavaScript 解决二分搜索问题

```javascript
