  let minSum = Infinity;
  let currentSum = 0;

  for (let i = 0; i < nums.length; i++) {
    currentSum += nums[i];
    if (currentSum < minSum) {
      minSum = currentSum;
    }
    if (currentSum > 0) {
      currentSum = 0;
    }
  }

  return minSum;
}



