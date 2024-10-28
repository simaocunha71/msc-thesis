  const mean = numbers.reduce((sum, x) => sum + x, 0) / numbers.length;
  const deviation = numbers.map(x => Math.abs(x - mean)).reduce((sum, x) => sum + x, 0);
  return deviation / numbers.length;
}



