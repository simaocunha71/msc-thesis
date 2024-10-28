```
let minSum = Infinity;
let currentSum = 0;

for (let num of nums) {
  currentSum += num;
  minSum = Math.min(minSum, currentSum);
  if (currentSum > 0) {
    currentSum = 0;
  }
}

return minSum;
```
Explanation:
We use a sliding window approach to find the minimum sum. We initialize `minSum` to infinity and `currentSum` to 0. We then iterate through the array, adding each number to `currentSum`. We update `minSum` with the minimum of the current sum and `minSum`. If `currentSum` becomes positive, we reset it to 0 to start a new subarray. At the end, `minSum` will hold the minimum sum of any non-empty subarray. If the array is empty, `minSum` will still be infinity, which is correct since the sum of an empty array is undefined.