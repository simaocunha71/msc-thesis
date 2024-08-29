  let sum = 0;
  let mean = 0;
  for (const n of numbers) {
    sum += n;
  }
  mean = sum / numbers.length;
  for (const n of numbers) {
    sum += Math.abs(n - mean);
  }
  return sum / numbers.length;
}



