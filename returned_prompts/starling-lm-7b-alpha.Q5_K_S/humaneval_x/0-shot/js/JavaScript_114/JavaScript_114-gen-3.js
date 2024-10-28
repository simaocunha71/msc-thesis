To solve this problem, we can use a sliding window approach. We initialize a variable `minSum` to positive infinity and a variable `currentSum` to 0. Then we iterate over the array `nums` with a `for` loop. Inside the loop, we add the current element `nums[i]` to `currentSum`. If `currentSum` becomes greater than `minSum`, we update `minSum` to `currentSum`. If `currentSum` becomes negative, we reset it to 0. Finally, we return `minSum`.

Here is the detailed step-by-step explanation of the code:

1. We initialize `minSum` to positive infinity and `currentSum` to 0.
2. We iterate over the array `nums` using a `for` loop.
3. Inside the loop, we add the current element `nums[i]` to `currentSum`.
4. If `currentSum` becomes greater than `minSum`, we update `minSum` to `currentSum`.
5. If `currentSum` becomes negative, we reset it to 0.
6. After the loop, we return `minSum`.

The time complexity of this solution is O(n), where n is the length of the array `nums`. The space complexity is O(1), as we only use a constant amount of extra space.

The solution works by continuously updating the minimum sum as we process each number in the array. The sliding window approach allows us to efficiently find the minimum sum of any non-empty sub-array, as we only need to consider the current element and the previous elements in the window. By updating `minSum` whenever `currentSum` becomes smaller, we ensure that `minSum` always holds the smallest sum encountered so far.

It's worth noting that this solution may not be the most optimized one, but it is simple and easy to understand. There are more optimized solutions available, but they may be more complex.

Here's a code example of the solution in JavaScript:

```javascript
const minSubArraySum = (nums) => {
  let minSum = Infinity;
  let currentSum = 0;

  for (let i = 0; i < nums.length; i++) {
    currentSum +=