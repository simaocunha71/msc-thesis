  let minSum = Infinity;
  let curSum = 0;
  for (let i = 0; i < nums.length; i++) {
    curSum += nums[i];
    if (curSum < minSum) {
      minSum = curSum;
    }
    if (curSum < 0) {
      curSum = 0;
    }
  }
  return minSum;
}



