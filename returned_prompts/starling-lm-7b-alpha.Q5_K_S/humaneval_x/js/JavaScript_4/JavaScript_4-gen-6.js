  const M = mean(numbers);
  return numbers.map(x => Math.abs(x - M)).reduce((a, b) => a + b) / numbers.length;
}



