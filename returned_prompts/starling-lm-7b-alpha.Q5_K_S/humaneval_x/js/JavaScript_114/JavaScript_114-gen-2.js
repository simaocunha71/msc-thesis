  let minSum = Number.MAX_SAFE_INTEGER;
  let curSum = 0;
  for (const n of nums) {
    curSum += n;
    if (curSum < minSum) {
      minSum = curSum;
    } else if (curSum > minSum) {
      curSum = 0;
    }
  }
  return minSum;
}



