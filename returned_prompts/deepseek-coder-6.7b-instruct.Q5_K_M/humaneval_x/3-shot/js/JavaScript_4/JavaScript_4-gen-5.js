  let mean 
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  mean = sum / numbers.length;
  let deviation_sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    deviation_sum += Math.abs(numbers[i] - mean);
  }
  return deviation_sum / numbers.length;
}



