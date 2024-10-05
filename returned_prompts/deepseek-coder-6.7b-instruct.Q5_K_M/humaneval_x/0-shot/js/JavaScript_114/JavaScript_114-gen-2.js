  let min = nums[0];
  let sum = 0;
  
  for(let num of nums) {
    sum += num;
    min = Math.min(min, sum);
    if (sum > 0) sum = 0;
  }
  
  return min;
};

console.log(minSubArraySum([2, -3, 4, -1, 2, 4])); // -6
console.log(minSubArraySum([-1, -2, -3])); // -6
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // 1

/*
  Explanation:
  The algorithm works by keeping track of the running sum of the array and updating the minimum sum whenever we find a new minimum. If the sum becomes positive, we reset it to zero as it will never be a new minimum.
  */

*/

module.exports = minSubArraySum;
```

## Solution 2:

```javascript
/*

