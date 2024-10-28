  var minSum = nums[0];
  var currentSum = nums[0];

  for (var i = 1; i < nums.length; i++) {
    currentSum += nums[i];
    if (nums[i] < currentSum) {
      currentSum = nums[i];
    }
    if (currentSum < minSum) {
      minSum = currentSum;
    }
  }

  return minSum;
}



