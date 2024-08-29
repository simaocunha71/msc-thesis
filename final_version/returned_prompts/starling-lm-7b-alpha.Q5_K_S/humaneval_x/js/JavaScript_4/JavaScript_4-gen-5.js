  let mean = 0;
  let mad = 0;
  for (let i = 0; i < numbers.length; i++) {
    mean += numbers[i];
  }
  mean /= numbers.length;

  for (let i = 0; i < numbers.length; i++) {
    mad += Math.abs(numbers[i] - mean);
  }
  mad /= numbers.length;

  return mad;
}



