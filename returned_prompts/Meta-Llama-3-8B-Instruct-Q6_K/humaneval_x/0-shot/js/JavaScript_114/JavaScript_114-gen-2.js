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

  return Math.min(minSum, currentSum);
};
```


Explanation:
The idea is to keep track of the minimum sum of any non-empty sub-array. We initialize `minSum` to `Infinity` and `currentSum` to `0`. 

We iterate over the array, adding each number to `currentSum`. We update `minSum` with the minimum of `minSum` and `currentSum`. 

If `currentSum` becomes positive, we reset it to `0` to start a new sub-array. 

Finally, we return the minimum of `minSum` and `currentSum`. 

This solution has a time complexity of O(n) and a space complexity of O(1). 