  let minSum = Infinity;
  for (let left = 0, right = 0, currentSum = 0; right < nums.length; right++) {
    currentSum += nums[right];
    while (currentSum > minSum) {
      currentSum -= nums[left++];
    }
    minSum = Math.min(minSum, currentSum);
  }
  return minSum;
}