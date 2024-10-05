  let min = Infinity;
  let sum = 0;

  for (let i = 0; i < nums.length; i++) {
    sum = 0;
    for (let j = i; j < nums.length; j++) {
      sum += nums[j];
      min = Math.min(min, sum);
    }
  }

  return min;
};

console.log(minSubArraySum([2, 3, -4, 1, -2, 4])); // 1
console.log(minSubArraySum([-1, -2, -3])); // -6

*/

//Solution:
/*
The problem is to find the minimum sum of any non-empty sub-array of the given array.

Here is the solution using dynamic programming approach:

1. Initialize min as Infinity and sum as 0.
2. Iterate over the array from 0 to the end. For each index i, calculate the sum of the sub-array from index i to the end of the array.
3. Update min with the minimum of min and sum.
4. Return min.

This approach works because it finds the minimum sum of all possible non-empty sub-arrays of the given array and returns the minimum sum.
*/

//Time complexity: O(n^2)
//Space complexity: O(1)

//Note: This solution will not pass for arrays with negative numbers as it does not consider the minimum sub-array that can be made by summing only negative numbers. For that case, we would need to use Kadane's algorithm which is more efficient.

//Kadane's Algorithm:
//Iterate over the array and keep track of the running sum. If the running sum becomes negative, reset it to 0. Update the maximum sum seen so far. The answer to the problem would be the maximum sum seen so far.

//Time complexity: O(n)
//Space complexity: O(1)

//This algorithm runs in O(n) time complexity and O(1) space complexity because it only scans the array once and uses a constant amount of additional space.

const minSubArraySum = (nums) => {
 