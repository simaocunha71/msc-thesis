```
function minSubArraySum(nums) {
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
}
```

Explanation:
The problem is asking to find the minimum sum of any non-empty sub-array of the given array. We can solve this problem by using a sliding window approach.

We initialize two variables `minSum` and `currentSum` to infinity and 0 respectively. We then iterate over the array and for each number, we add it to `currentSum` and update `minSum` if the current sum is less than `minSum`. If `currentSum` becomes greater than 0, we reset `currentSum` to 0.

Finally, we return the minimum of `minSum` and 0. This is because the minimum sum of any non-empty sub-array cannot be less than 0.

The time complexity of this solution is O(n) where n is the length of the input array. The space complexity is O(1) as we are using a constant amount of space to store the variables.