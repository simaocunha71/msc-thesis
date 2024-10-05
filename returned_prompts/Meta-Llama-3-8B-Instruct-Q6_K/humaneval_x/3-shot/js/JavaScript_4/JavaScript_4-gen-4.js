  let mean = numbers.reduce((acc, curr) => acc + curr, 0) / numbers.length;
  let sum = 0;
  for (let num of numbers) {
    sum += Math.abs(num - mean);
  }
  return sum / numbers.length;
}
