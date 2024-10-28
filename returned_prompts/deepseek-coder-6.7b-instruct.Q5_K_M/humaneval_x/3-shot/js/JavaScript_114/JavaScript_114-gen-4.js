  let minSum = Number.MAX_SAFE_INTEGER;
  let currentSum = 0;

  for (let num of nums) {
    currentSum += num;
    minSum = Math.min(minSum, currentSum);
    currentSum = Math.min(currentSum, num);
  }

  return minSum;
}



