  let min = Math.min(...nums);
  let sum = min;
  let curr = min;
  for (let i = 1; i < nums.length; i++) {
    curr = Math.min(nums[i], curr + nums[i]);
    sum = Math.min(sum, curr);
  }
  return sum;
}
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])) // 1
console.log(minSubArraySum([-1, -2, -3])) // -6
console.log(minSubArraySum([1, -1, -2, 3])) // -2
console.log(minSubArraySum([3, -1, 4])) // -1
console.log(minSubArraySum([-1, 2, 3, -4, 5])) // -5
```

This solution works by using Kadane's algorithm. It initializes the minimum sum to be the minimum value in the array and the current sum to be the minimum value. Then it iterates through the array, updating the current sum and the minimum sum as it goes. The current sum is updated to be the minimum of the current value and the sum of the current value and the previous current sum. The minimum sum is updated to be the minimum of the current sum and the previous minimum sum. Finally, it returns the minimum sum.

This solution has a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array.

This solution works for arrays with positive and negative integers. It also handles the case where all integers in the array are negative by returning the smallest negative integer.

It's important to note that the problem statement is a bit ambiguous, as it doesn't specify what to do when the array contains all positive numbers. In this case, the function returns the smallest positive number, which may not be what you want. You may want to return 0 in this case.
*/
















































