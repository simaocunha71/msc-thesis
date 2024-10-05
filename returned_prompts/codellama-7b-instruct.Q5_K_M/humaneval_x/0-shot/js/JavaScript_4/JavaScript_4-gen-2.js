const meanAbsoluteDeviation = (numbers) => {
  const mean = numbers.reduce((a, b) => a + b) / numbers.length;
  const deviation = numbers.map((n) => Math.abs(n - mean));
  const sum = deviation.reduce((a, b) => a + b);
  return sum / numbers.length;
};

