  let mean = mean(numbers);
  let mad = 0;

  for (let i = 0; i < numbers.length; i++) {
    mad += Math.abs(numbers[i] - mean);
  }

  return mad / numbers.length;
}



