  let mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  let sum = 0;
  for (const num of numbers) {
    sum += Math.abs(num - mean);
  }
  return sum / numbers.length;
}