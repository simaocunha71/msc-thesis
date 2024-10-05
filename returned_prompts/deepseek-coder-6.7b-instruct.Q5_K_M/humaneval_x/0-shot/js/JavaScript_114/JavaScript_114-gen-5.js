  let sum = Infinity;
  let curSum = 0;

  for(let num of nums) {
    curSum = Math.min(curSum + num, num);
    sum = Math.min(sum, curSum);
  }

  return sum;
};

console.log(minSubArraySum([2, -3, 4, -1, 2, 4])); // 1
console.log(minSubArraySum([-1, -2, -3])); // -6
console.log(minSubArraySum([1, 2, 3, 4])); // 1
console.log(minSubArraySum([-1, -2, 3, -4])); // -6
console.log(minSubArraySum([-1, -2, 3, 4])); // -1
console.log(minSubArraySum([1, 2, 3, -4])); // 1
console.log(minSubArraySum([-2, 1, -3, 4, -1, 2, 1])); // -6
console.log(minSubArraySum([1, -2, 3, -4, -1, 2, 4])); // -1
console.log(minSubArraySum([-1, 2, -3, 4, -1, 2, 4])); // 1
console.log(minSubArraySum([-1, 2, -3, 4, -1, 2, -4])); // -6

*/

This problem is known as the Minimum Subarray Sum problem. It's a dynamic programming problem where we keep track of the minimum sum of a non-empty subarray. We use a variable 'sum' to keep track of the minimum sum and 'curSum' to keep track of the current sum. We iterate through the array and at each step, we update 'curSum' and 'sum' based on whether the current number is smaller or equal to the current sum plus the current number. The minimum sum of a non-empty subarray is then 'sum'.

The time complexity is O(n) and the space complexity is O(1), where n is the length of