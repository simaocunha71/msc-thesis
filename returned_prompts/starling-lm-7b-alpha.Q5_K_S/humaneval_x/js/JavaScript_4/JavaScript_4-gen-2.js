  let sum = 0;
  let mean = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += Math.abs(numbers[i]);
    mean += numbers[i];
  }
  mean /= numbers.length;
  return sum / numbers.length;
}



