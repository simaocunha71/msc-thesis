  let mean = 0;
  for (let i = 0; i < numbers.length; i++) {
    mean += numbers[i];
  }
  mean /= numbers.length;

  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += Math.abs(numbers[i] - mean);
  }
  return sum / numbers.length;
}