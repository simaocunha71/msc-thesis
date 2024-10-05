  let mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  let sum = numbers.reduce((a, b) => a + Math.abs(b - mean), 0);
  return sum / numbers.length;
}



