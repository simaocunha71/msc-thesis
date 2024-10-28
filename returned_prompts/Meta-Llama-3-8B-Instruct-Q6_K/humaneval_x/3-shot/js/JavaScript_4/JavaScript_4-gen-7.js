  let mean = numbers.reduce((a, b) => a + b) / numbers.length;
  let sum = 0;
  for (let num of numbers) {
    sum += Math.abs(num - mean);
  }
  return sum / numbers.length;
}