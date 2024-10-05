  let mean = numbers.reduce((a, b) => a + b) / numbers.length;
  let deviations = numbers.map((x) => Math.abs(x - mean));
  return deviations.reduce((a, b) => a + b) / numbers.length;
}