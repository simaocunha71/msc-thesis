  let sum = 0;
  for (const num of numbers) {
    sum += num;
  }
  let mean = sum / numbers.length;
  let sum_abs = 0;
  for (const num of numbers) {
    sum_abs += Math.abs(num - mean);
  }
  return sum_abs / numbers.length;
}



