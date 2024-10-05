To solve this problem, we can use the concept of Kadane's algorithm, which is used to find the maximum sum subarray of a given array. By applying this algorithm, we can find the minimum sum subarray in O(n) time complexity, where n is the length of the input array.

Here's how the solution works:

1. Initialize a variable `minSum` with a large value, such as `Number.MAX_SAFE_INTEGER`. This will be used to store the minimum sum of the subarray.

2. Initialize a variable `currentSum` with 0. This will be used to keep track of the sum of the current subarray.

3. Iterate through the `nums` array using a for loop. For each element `num` in the array, do the following:

   a. Add the current element `num` to the `currentSum`.
   
   b. If the `currentSum` becomes less than 0, it means that the current subarray is not contributing positively to the sum. In this case, reset the `currentSum` to 0, as starting a new subarray may give a better result.
   
   c. If the `currentSum` is less than the `minSum`, update the `minSum` with the `currentSum`. This ensures that we are always keeping track of the minimum sum subarray.

4. After iterating through all elements in the array, return the `minSum`, which represents the minimum sum of any non-empty subarray of the `nums` array.

The time complexity of this solution is O(n), where n is the length of the input array, as we iterate through the array once. The space complexity is O(1), as we only use a fixed number of variables.

Here's an example implementation of the solution in JavaScript:

```javascript
const minSubArraySum = (nums) => {
  let minSum = Number.MAX_SAFE_INTEGER;
  let currentSum = 0;

  for (let num of nums) {
    currentSum += num;

    if (currentSum < 0) {
      currentSum = 0;
    } else if (currentSum < minSum) {
      minSum = currentSum;