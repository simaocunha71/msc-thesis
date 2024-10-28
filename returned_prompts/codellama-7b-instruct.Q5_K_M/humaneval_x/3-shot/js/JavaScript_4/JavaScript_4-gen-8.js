  let sum = 0;
  let mean = numbers.reduce((a, b) => a + b) / numbers.length;

  for (let i = 0; i < numbers.length; i++) {
    sum += Math.abs(numbers[i] - mean);
  }

  return sum / numbers.length;
}



