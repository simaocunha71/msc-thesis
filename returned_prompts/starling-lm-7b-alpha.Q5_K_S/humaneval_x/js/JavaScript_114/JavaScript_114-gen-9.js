  let min = Number.MAX_VALUE;
  let sum = 0;
  for (const n of nums) {
    sum += n;
    if (sum < min) {
      min = sum;
    }
    if (sum < 0) {
      sum = 0;
    }
  }
  return min;
}



