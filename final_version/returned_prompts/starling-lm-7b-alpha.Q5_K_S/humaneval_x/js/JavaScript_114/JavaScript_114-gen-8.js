  let minSum = Infinity;
  let currSum = 0;
  for (let i = 0; i < nums.length; i++) {
    currSum += nums[i];
    if (currSum < minSum) {
      minSum = currSum;
    } else if (currSum > 0) {
      currSum = 0;
    }
  }
  return minSum;
}



