  let mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += Math.abs(numbers[i] - mean);
  }
  return sum / numbers.length;
} 



