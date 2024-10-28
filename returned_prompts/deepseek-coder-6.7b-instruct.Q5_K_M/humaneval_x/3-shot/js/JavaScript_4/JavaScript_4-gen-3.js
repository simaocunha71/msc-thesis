  let mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  return numbers.map(num => Math.abs(num - mean)).reduce((a, b) => a + b, 0) / numbers.length;
}



