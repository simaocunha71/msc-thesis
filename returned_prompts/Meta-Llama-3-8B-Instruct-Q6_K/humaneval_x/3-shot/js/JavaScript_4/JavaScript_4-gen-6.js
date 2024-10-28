  let sum = 0;
  let mean = 0;
  for (const num of numbers) {
    mean += num;
  }
  mean /= numbers.length;
  for (const num of numbers) {
    sum += Math.abs(num - mean);
  }
  return sum / numbers.length;
}