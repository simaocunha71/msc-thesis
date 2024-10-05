  let mean = 0;
  for (let num of numbers) {
    mean += num;
  }
  mean /= numbers.length;

  let mad = 0;
  for (let num of numbers) {
    mad += Math.abs(num - mean);
  }
  mad /= numbers.length;

  return mad;
}