const mean = numbers => numbers.reduce((a, b) => a + b) / numbers.length;
const deviation = numbers => numbers.map(x => Math.abs(x - mean(numbers)));
const mad = numbers => deviation(numbers).reduce((a, b) => a + b) / numbers.length;

  return mad(numbers);
};
