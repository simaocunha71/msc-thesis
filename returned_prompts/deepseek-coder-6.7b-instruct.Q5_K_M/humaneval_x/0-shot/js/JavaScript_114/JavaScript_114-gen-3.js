  let min = Infinity;
  let curSum = 0;
  for (let num of nums) {
    curSum += num;
    min = Math.min(min, curSum);
    if (curSum > 0) curSum = 0;
  }
  return min;
};

console.log(minSubArraySum([2, -3, 4, -1, 2, 4])); //-6
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); //1
console.log(minSubArraySum([-1, -2, -3])); //-6
console.log(minSubArraySum([3, -2, 4, -1, 5])); //-6
console.log(minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4])); //-8
```

## 3. Substring with At Least K Repeating Characters

