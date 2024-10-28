  let minSum = Infinity, runningSum = 0;
  for (let num of nums) {
    runningSum += num;
    minSum = Math.min(minSum, runningSum);
    runningSum = Math.min(runningSum, 0);
  }
  return minSum;
}



