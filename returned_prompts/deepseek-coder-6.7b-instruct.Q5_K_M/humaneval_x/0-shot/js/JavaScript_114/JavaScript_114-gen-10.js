  let total = 0, minSubArray = Infinity;

  for (let i = 0; i < nums.length; i++) {
    total += nums[i];
    minSubArray = Math.min(minSubArray, total);
    total = Math.min(total, nums[i]);
  }

  return minSubArray;
}

console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // 1
console.log(minSubArraySum([-1, -2, -3])); // -6

```

### Explanation

We keep a running total and keep updating it with each iteration. Also, we keep track of the minimum sum so far in the variable `minSubArray`.

In every iteration, we update `minSubArray` with the minimum of `minSubArray` and `total`. After that, we update `total` with the minimum of `total` and `nums[i]`.

In the end, we return `minSubArray` which would be the minimum sum of any non-empty sub-array of `nums`.

### Complexity

This solution has a time complexity of O(n), and a space complexity of O(1).

### Test Cases

```javascript
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // Expected output: 1
console.log(minSubArraySum([-1, -2, -3])); // Expected output: -6
console.log(minSubArraySum([1, 2, 3, 4, 5])); // Expected output: 1
console.log(minSubArraySum([-2, -3, -1])); // Expected output: -3
```

These test cases check the functionality of the code for different types of inputs. The first two test cases check for negative numbers, the next two test cases check for positive numbers. The function should return the smallest sum for each of these test cases.

### Edge Cases

The function should handle edge cases properly. For example, if the input is an empty array, the function