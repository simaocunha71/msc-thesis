To solve this problem, we can follow these steps:

1. Initialize a variable minSum to the sum of the first element in the array. This will serve as the minimum sum we have found so far.
2. Initialize a variable sum to the sum of the first element in the array as well. This will be used to keep track of the sum of the subarray we are currently considering.
3. Iterate through the array starting from the second element. For each element, we will update the sum by adding the current element and subtracting the previous element.
4. After updating the sum, we will compare it to the current minimum sum (minSum). If the updated sum is smaller than the current minimum sum, we will update minSum to the updated sum.
5. Finally, we will return the minimum sum (minSum).

Here's the implementation of the solution:

const minSubArraySum = (nums) => {
  let minSum = nums[0];
  let sum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    sum = sum + nums[i];
    if (sum < minSum) minSum = sum;
    if (sum < 0) sum = 0;
  }

  return minSum;
};

This implementation has a time complexity of O(n), where n is the length of the input array, as we only iterate through the array once. The space complexity is O(1), as we only use a constant amount of additional memory.

The solution correctly handles the case of an empty array by returning 0, as the minimum sum of an empty subarray is 0.

Additionally, the solution correctly handles the case of a single-element array by returning the value of the single element, as the minimum sum of a single-element subarray is the value of the element itself.

Overall, this solution provides a concise and efficient approach to finding the minimum sum of any non-empty subarray of the given input array.

*/

/*
  Given an array of integers nums, find the minimum sum of any non-empty sub-array
  of nums.
  Example
  minSubArraySum([2, 3, 4, 1, 2