  var minSum = 0;
  var currentSum = 0;
  for (var i = 0; i < nums.length; i++) {
    currentSum += nums[i];
    minSum = Math.min(minSum, currentSum);
    if (currentSum < 0) {
      currentSum = 0;
    }
  }
  return minSum;
}



