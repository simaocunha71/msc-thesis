  const mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  const deviations = numbers.map(num => Math.abs(num - mean));
  return deviations.reduce((a, b) => a + b, 0) / numbers.length;
}



