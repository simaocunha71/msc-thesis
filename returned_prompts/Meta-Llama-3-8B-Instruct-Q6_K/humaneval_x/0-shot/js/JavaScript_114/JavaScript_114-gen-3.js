```
const minSubArraySum = (nums) => {
  let minSum = Infinity;
  let currentSum = 0;

  for (let num of nums) {
    currentSum += num;
    minSum = Math.min(minSum, currentSum);
    if (currentSum > 0) {
      currentSum = 0;
    }
  }

  return Math.min(minSum, 0);
};
```


Explanation:
The problem asks to find the minimum sum of any non-empty sub-array of the given array. This can be solved by iterating through the array and updating the minimum sum whenever a new sub-array sum is calculated.

We initialize two variables: `minSum` to store the minimum sum found so far (set to infinity initially), and `currentSum` to store the sum of the current sub-array (set to 0 initially).

In the loop, we iterate through the array and add each number to `currentSum`. We update `minSum` with the minimum of the current `minSum` and `currentSum`. If `currentSum` becomes greater than 0, we reset it to 0 to start a new sub-array.

Finally, we return the minimum of `minSum` and 0, as the minimum sum cannot be negative. This is because the problem statement asks for the minimum sum of any non-empty sub-array, and an empty sub-array would have a sum of 0.

The time complexity of this solution is O(n), where n is the length of the input array, as we iterate through the array once. The space complexity is O(1), as we only use a constant amount of space to store the variables.