  let sum = 0, minSum = Infinity;
  for (let num of nums) {
    sum += num;
    minSum = Math.min(minSum, sum);
    if (sum > 0) sum = 0;
  }
  return minSum;
}



