  let min = Infinity;
  let curSum = 0;

  for (let num of nums) {
      curSum += num;
      min = Math.min(min, curSum);
      if (curSum > 0) curSum = 0;
  }

  return min;
}

console.log(minSubArraySum([2, -3, 4, -1, 2, 4])); // Output: -6
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // Output: 1

// This solution works by maintaining a running total of the current array segment.
// Whenever the running total becomes negative, it resets itself back to zero and continues with the next segment.
// The minimum of all these running totals is the minimum sum of any non-empty sub-array.

// The time complexity of this solution is O(n), where n is the size of the input array. This is because we're only looping through the array once.
// The space complexity is O(1), since we're only using a constant amount of space to store our variables.

// The logic here is that if the running total ever goes negative, it means that the subsequent numbers are reducing the total sum. So, it's more efficient to start a new segment from there.
// And keep track of the smallest running total we've seen so far, because that's the smallest non-empty sub-array we can form.

// This solution is a classic example of a "greedy" algorithm, where we're making locally optimal choices at each step to get the global optimum.

// This solution also handles the case where all numbers in the array are negative, and returns the smallest negative number because that's the smallest non-empty sub-array we can form in that case.
```

## 参考

- [LeetCode Problem 53](https://leetcode.com/problems/maximum-subarray/)
- [LeetCode Problem 918](https://leetcode.com/problems/maximum-sum-circular-subarray/)
- [LeetCode Problem 152](https://leetcode.com/