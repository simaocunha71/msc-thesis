  let sum = 0;
  let n = numbers.length;
  let mean = numbers.reduce((a, b) => a + b, 0) / n;

  for (let i = 0; i < n; i++) {
    sum += Math.abs(numbers[i] - mean);
  }

  return sum / n;
}



