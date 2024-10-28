  const mean = numbers.reduce((p, c) => p + c, 0) / numbers.length;
  const deviations = numbers.map(n => Math.abs(n - mean));
  const sum = deviations.reduce((p, c) => p + c, 0);
  return sum / numbers.length;
}



