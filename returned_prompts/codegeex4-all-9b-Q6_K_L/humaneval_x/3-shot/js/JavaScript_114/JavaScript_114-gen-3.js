  let minSum = Infinity;
  for (let i = 0; i < nums.length; i++) {
    let currentSum = nums[i];
    if (currentSum < minSum) {
      minSum = currentSum;
    }
    for (let j = i + 1; j < nums.length; j++) {
      currentSum += nums[j];
      if (currentSum < minSum) {
        minSum = currentSum;
      }
    }
  }
  return minSum;
}