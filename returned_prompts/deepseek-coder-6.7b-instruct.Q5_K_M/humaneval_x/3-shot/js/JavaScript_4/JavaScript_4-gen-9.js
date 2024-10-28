  let mean = numbers.reduce((a, b) => a + b) / numbers.length;
  return numbers.reduce((a, b) => a + Math.abs(b - mean), 0) / numbers.length;
}



